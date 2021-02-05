from bipwallet import wallet, utils


def gen_address(index):

    # Ваша seed фраза
    myseed = wallet.generate_mnemonic()
    seed = 'point outside brother august labor warfare ten short amazing meadow library noodle'

    # Мастер ключ из seed фразы
    master_key = utils.HDPrivateKey.master_key_from_mnemonic(seed)

    # public_key из мастер ключа по пути 'm/44/0/0/0'
    root_keys = utils.HDKey.from_path(
      master_key, "m/44'/0'/0'/0")[-1].public_key.to_b58check()

    # Адрес дочернего кошелька в зависимости от значения index
    address = utils.Wallet.deserialize(
      root_keys, network='BTC').get_child(index, is_prime=False).to_address()

    rootkeys_wif = utils.HDKey.from_path(
      master_key, f"m/44'/0'/0'/0/{index}")[-1]

    # Extended private key
    xprivatekey = rootkeys_wif.to_b58check()

    # Wallet import format
    wif = utils.Wallet.deserialize(xprivatekey, network='BTC').export_to_wif()

    return address, wif


print(gen_address(1))
