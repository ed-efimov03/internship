def minable_required(func):
    """
    Декоратор, который проверяет, можно ли майнить криптовалюту.
    Если криптовалюта не майнится, выводит сообщение.
    """
    def wrapper(crypto):
        if not crypto.minable:
            print(f"{crypto} не майнится.")
            return None  
        return func(crypto)
    return wrapper


class Cryptocurrency:
    """Базовый класс для криптовалют."""
    
    def __init__(self, name, symbol, minable, rate_to_usd, anonymous):
        self.name = name 
        self.symbol = symbol  
        self.minable = minable 
        self.rate_to_usd = rate_to_usd 
        self.anonymous = anonymous  

    def mining_reward(self):
        """Метод для получения награды за майнинг (не реализован в базовом классе)."""
        return None  
    
    def __str__(self):
        """Возвращает строковое представление криптовалюты."""
        return f"{self.name} ({self.symbol})" 


class Nano(Cryptocurrency):
    """Класс для криптовалюты Nano."""
    
    def __init__(self, block_lattice=False, rate_to_usd=5, anonymous=True):
        super().__init__("Nano", "NANO", True, rate_to_usd, anonymous)
        self.block_lattice = block_lattice 

    @minable_required
    def mining_reward(self):
        """Возвращает награду за майнинг для Nano."""
        return 0.02 if self.block_lattice else 0.01  


class Iota(Cryptocurrency):
    """Класс для криптовалюты Iota."""
    
    def __init__(self, tangle=False, rate_to_usd=0.3, anonymous=False):
        super().__init__("Iota", "IOTA", True, rate_to_usd, anonymous)
        self.tangle = tangle  

    @minable_required
    def mining_reward(self):
        """Возвращает награду за майнинг для Iota."""
        return 0.001 if self.tangle else 0.002  


class Stellar(Cryptocurrency):
    """Класс для криптовалюты Stellar."""
    
    def __init__(self, distributed=False, rate_to_usd=0.1, anonymous=True):
        super().__init__("Stellar", "XLM", False, rate_to_usd, anonymous)
        self.distributed = distributed  

    def mining_reward(self):
        """Stellar не майнится, поэтому метод возвращает None."""
        return None 


def print_info(crypto: Cryptocurrency):
    """Выводит информацию о криптовалюте."""
    
    minable_str = 'добывают майнингом' if crypto.minable else 'не майнится'
    anonymity_str = 'анонимные транзакции' if crypto.anonymous else 'только публичные транзакции'
    
    # Собираем дополнительные особенности криптовалюты
    additional_info = [
        'блок-решетка' if getattr(crypto, 'block_lattice', False) else '',
        'Tangle' if getattr(crypto, 'tangle', False) else '',
        'распределенная сеть' if getattr(crypto, 'distributed', False) else ''
    ]
    additional_str = ', '.join(filter(None, additional_info)) or 'без особенностей'
    
    # Выводим информацию о криптовалюте
    print(f"{crypto}: {minable_str}, курс к USD: {crypto.rate_to_usd}, {anonymity_str}, {additional_str}")


cryptocurrencies = [
    Nano(block_lattice=True, rate_to_usd=6, anonymous=False),
    Iota(tangle=True, rate_to_usd=0.4, anonymous=False),
    Stellar(distributed=True, rate_to_usd=0.15, anonymous=True)
]

# Выводим информацию о криптовалютах и их награде за майнинг (если применимо)
for crypto in cryptocurrencies:
    print_info(crypto)
    if crypto.minable:
        reward = crypto.mining_reward()
        if reward is not None:
            print(f"Награда за майнинг: {reward} {crypto.symbol}\n")
