from bip_utils import Bip39SeedGenerator, Bip44Coins, Bip44, base58, Bip44Changes
import pandas as pd
# 导入配置文件中的参数
import config

class BlockChainAccount():

    def __init__(self, mnemonic, coin_type=Bip44Coins.ETHEREUM, password='', num=1) -> None:

        self.mnemonic = mnemonic.strip()
        self.coin_type = coin_type
        self.password = password # if have password
        self.num = num

    def get_address_pk(self):
        wallets = []
        for i in range(self.num):

            seed_bytes = Bip39SeedGenerator(self.mnemonic).Generate(self.password)
            # if self.coin_type != Bip44Coins.SOLANA:
            #     bip44_mst_ctx = Bip44.FromSeed(seed_bytes, self.coin_type).DeriveDefaultPath()
            #     return bip44_mst_ctx.PublicKey().ToAddress(), bip44_mst_ctx.PrivateKey().Raw().ToHex()
            # else:
            bip44_mst_ctx = Bip44.FromSeed(seed_bytes, self.coin_type)
            bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(i)
            bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT) # if you use "Solflare", remove this line and make a simple code modify and test
            priv_key_bytes = bip44_chg_ctx.PrivateKey().Raw().ToBytes()
            public_key_bytes = bip44_chg_ctx.PublicKey().RawCompressed().ToBytes()[1:]
            key_pair = priv_key_bytes+public_key_bytes
            wallet_info =  {'Wallet': f'Wallet-{i+1}', 'Address': bip44_chg_ctx.PublicKey().ToAddress(), 'PriveteKey': base58.Base58Encoder.Encode(key_pair)}
            wallets.append(wallet_info)
        df = pd.DataFrame(wallets)
        df.to_csv('./data/output/solana_wallets.csv', index=False)
        


coin_types = {
    # Bip44Coins.ETHEREUM: 'ethereum(evm)',
    Bip44Coins.SOLANA: 'solana',
    # Bip44Coins.TERRA: 'luna',
    # Bip44Coins.DASH: 'dash',
    # .....
    # also support other chain, such as file coin, eth classic, doge, dash, luna ....
    # example change coin_type as Bip44Coins.EOS, Bip44Coins.TERRA .....
}
for coin_type in coin_types.keys():
    chain_name = coin_types[coin_type]
    bca = BlockChainAccount(mnemonic=config.mnemonic, coin_type=coin_type, num=config.create_amount)
    bca.get_address_pk()

