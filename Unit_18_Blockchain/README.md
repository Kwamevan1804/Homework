# <span style="color:yellow">Instructions for Zblock!</span> 

We have set up a blockchain testnet for Zbank called zblock in order to test blockchain functionality. This document outlines how to start the network.

## <span style="color:green">Creating the zblock network</span>

The zblock network has been set up using puppeth, a helper tool from the geth (Go Ethereum) library for managing private blockchains. Puppeth is saved in the Blockchain-Tools folder. We seeded the network with a genesis block that uses Clique proof-of-authority to add blocks to the blockchain:

Created new network 'zblock' via ./puppeth:  
ChainID: 2072  
Proof-of-Authority  
Blocktime: every 15 seconds  

## <span style="color:green">Creating the network nodes</span>
Using the geth command-line tool, we created the following two nodes on the network which have been initialized with the zblock genesis block:

node_hw1
Public address of the key:   0xaAEe663C13b6af1d88aF9B9011508D20de446B72

node_hw2
Public address of the key:   0xF7081bdA5D5258dE0a6a066E091bA396Ff30b117

## <span style="color:green">Starting the network</span>
To start the network, in Terminal please navigate to the Blockchain-Tools folder which contains the node data. First start node 1 as a full mining node on the zblock network using the following command: 

    ./geth --datadir node_hw1 --unlock "aAEe663C13b6af1d88aF9B9011508D20de446B72" --rpc --mine --miner.threads 1 --ipcdisable --allow-insecure-unlock

This geth command calls node_hw1 in unlocked mode and exposes it to rpc (--rpc: Remote Procedural Call) a network element to facilitate node communication which allows us to use apps like MyCrypto which we'll do below. The node is set up as a mining node with the flags '--mine --miner.threads 1'. The flags '--ipcdisable' and '--allow-insecure-unlock' disable select security features.

After executing the command, wait while the node is initialized and initial output is generated on the screen. After about 30-60 seconds the message 'looking for peers' should appear repeatedly.

Find the output that starts with 'enode://' followed by a hash string and copy this code. You'll use this code to start the second node with this command:

    ./geth --datadir node_hw2 --unlock "F7081bdA5D5258dE0a6a066E091bA396Ff30b117" --port 30304 --bootnodes "enode://CORRECT ENODE ADDRESS HERE" --mine --miner.threads 1 --allow-insecure-unlock --ipcdisable

This geth command starts the second node, node_hw2, also in an unlocked mode. It assigns a subsequent port 30304 as 30303 is already used by the first node. The '--bootnodes' flag stipulates the other nodes that are part of the network via the enode address. This node is also set up as a miner node with the "--mine --miner.threads 1" flags.

After executing the command, similar output will be generated on screen. After about 30-60 seconds the message 'looking for peers' should appear repeatedly.

## <span style="color:green">Sending transactions via MyCrypto</span>
We will use the wallet application MyCrypto to send a test transaction. Open MyCrypto wallet and click on Keystore File to open the first node. 

<img src="README screenshots/MyCrypto 1.png" width=700 height=300 />

When prompted select the keystore file under Blockchain-Tools/node_hw1/ and enter the password:

<img src="README screenshots/MyCrypto Keystore file.png" width=700 height=300 />

Now enter the public address of the second node node_hw2 and the amount of ETH to send (100), then hit Send Transaction and confirm: 

<img src="README screenshots/MyCrypto Send tx.png" width=700 height=300 />

After confirming the transaction, click on Check TX Status:

<img src="README screenshots/MyCrypto Check tx.png" width=700 height=300 />

After clicking on logout you can see the successful transaction status:

<img src="README screenshots/MyCrypto Tx status.png" width=700 height=300 />

You can check the balance of node_hw1 by logging back in with the keystore file as explained above, and see how the balance has decreased by 100 ETH. Congratulations! You've just sent your first transaction on the blockchain.