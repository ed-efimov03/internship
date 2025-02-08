def minable_required(func):
    def wrapper(crypto):
        if not crypto.minable:
            print(f"{crypto} не майнится.")
            return None  
        return func(crypto)
    return wrapper


class Cryptocurrency:
    def __init__(self, name, symbol, minable, rate_to_usd, anonymous):
        self.name = name 
        self.symbol = symbol  
        self.minable = minable 
        self.rate_to_usd = rate_to_usd 
        self.anonymous = anonymous  

    def mining_reward(self):
        return None  
    
    def __str__(self):
        return f"{self.name} ({self.symbol})" 


class Nano(Cryptocurrency):
    def __init__(self, block_lattice=False, rate_to_usd=5, anonymous=True):
        super().__init__("Nano", "NANO", True, rate_to_usd, anonymous)
        self.block_lattice = block_lattice 

    @minable_required
    def mining_reward(self):
        return 0.02 if self.block_lattice else 0.01  


class Iota(Cryptocurrency):
    def __init__(self, tangle=False, rate_to_usd=0.3, anonymous=False):
        super().__init__("Iota", "IOTA", True, rate_to_usd, anonymous)
        self.tangle = tangle  

    @minable_required
    def mining_reward(self):
        return 0.001 if self.tangle else 0.002  


class Stellar(Cryptocurrency):
    def __init__(self, distributed=False, rate_to_usd=0.1, anonymous=True):
        super().__init__("Stellar", "XLM", False, rate_to_usd, anonymous)
        self.distributed = distributed  

    def mining_reward(self):
        return None 


def print_info(crypto: Cryptocurrency):
    minable_str = 'добывают майнингом' if crypto.minable else 'не майнится'
    anonymity_str = 'анонимные транзакции' if crypto.anonymous else 'только публичные транзакции'
    
    additional_info = []
    if hasattr(crypto, 'block_lattice') and crypto.block_lattice:
        additional_info.append('блок-решетка')
    if hasattr(crypto, 'tangle') and crypto.tangle:
        additional_info.append('Tangle')
    if hasattr(crypto, 'distributed') and crypto.distributed:
        additional_info.append('распределенная сеть')

    additional_str = ', '.join(additional_info) if additional_info else 'без особенностей'
    
    print(f"{crypto}: {minable_str}, курс к USD: {crypto.rate_to_usd}, {anonymity_str}, {additional_str}")


cryptocurrencies = [
    Nano(block_lattice=True, rate_to_usd=6, anonymous=False),
    Iota(tangle=True, rate_to_usd=0.4, anonymous=False),
    Stellar(distributed=True, rate_to_usd=0.15, anonymous=True)
]


for crypto in cryptocurrencies:
    print_info(crypto)
    if crypto.minable:
        reward = crypto.mining_reward()
        if reward:
            print(f"Награда за майнинг: {reward} {crypto.symbol}\n")
