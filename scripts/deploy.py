from brownie import WavePortal, accounts, network, config

def getAccount():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def main():
    account = getAccount()
    wp = WavePortal.deploy({'from':account})

    account.transfer(wp, '1 ether'); 

    #print('Initial count: ' + str(wp.getWaves()))
    #wp.wave()
    #print('Final count: ' + str(wp.getWaves()))