# BlockChain Mockup Program

This is a simple blockchain program used to help understanding and utilization of the data structures used for cryptocurrencies. This program does require some base knowledge on blocks, blockchains, and hashing. Provided below are the resources I have used for my first understanding of these topics. 

This program includes methods for: The creation of blocks, the hashing of blocks, the string representation of a block, the creation of a blockchain, the addition of blocks to a blockchain through mining, the printing of a blockchain, the updating of a blockchain. Any other methods are not officially supported but can be created to add further functionality. 

### Prerequisites

The following software is required to run this program:

    ```
    Python Version 2.7 or later
    ```

    ```
    Pysha3 Version 1.0.2
    ```

### Installation and Running 

1. Clone the repository

2. Create a Python Virtual Environment: 

    On Windows:

    Open the desired location of your virtual environment in the command prompt and run the following line, where 'environment_name' is the desired named of your virtual environment:

    ```
    python -m venv environment_name
    ```

    On Mac/Linux:

    Open the desired location of your virtual environment in the terminal and run the following line, where 'environment_name' is the desired named of your virtual environment:

    ```
    $ python3 -m venv environment_name
    ```

3. Activate the Virtual Environment:

    On Windows:

    Run the following command in the directory of the repository in the command prompt:

    ```
    environment_name\Scripts\activate.bat
    ```

    On Mac/Linux:

    Run the following command in the directory of your virtual environment in the terminal:

    ```
    $ source environment_name/bin/activate
    ```

4. Download the prerequisites listed in requirements.txt using the following line of code:

    ```
    $ pip install -r requirements.txt
    ```

    To verify that the requirements are installed you may run:

    ```
    $ pip list
    ```

5. Run main.py

    Windows:

    Run the following code in the repository's directory in the terminal:

    ```
    python main.py
    ```

    Mac/Linux:

    Run the following code in the repository's directory in the terminal:

    ```
    $ python3 main.py
    ```

    You may also run the code in any IDE that supports Python aslong as scripts are enabled on your system. 


## Modifying the Program

When modifying the program it is important to utilize the features these key variables provide:

    Nonce: 
    An arbitrary number used to create differences between hashes to find a hash that fits within the target. The nonce is added to the hash and if the hash is not accepted, it is changed so the overall hash will change, eventually finding a hash that fits within the target. 

    Max Nonce: 
    This is the maximum nonce that restricts the number of times hashing can be attempted for a block. In this program the max nonce is calculated by 2 to the power of the bytesize of the hash. For sha-256 because it is a 32 byte hash this is calculated by doing 2^32. Any suitably high number works for a max nonce. 

    POW: 
    This is the proof of work being utilized in the mining and hashing of the block. Proof of work is utilized to determine if a hash will be accepted or not.
    This is done by setting a Target with a Difficulty (See Below) to judge hashed data on. If the hash is less than the target hash then it is accepted and the block is added to the blockchain. This is required to prevent malicious altering of the blockchain which is most commonly done through 'double-spending' where users attempt to spend a certain amount of cryptocurrency twice in order to trick a user into believing they have received the amount of cryptocurrency. 

    Difficulty: 
    This is the difficulty of the target hash. This amount is subtracted from 8 times the bytesize of the hash. A larger difficulty will require more hashes to be performed to find an accepted hash. 

    Target: 
    This is the target hash used to compare other hashes to. If a hash is smaller than the target hash it is accepted. The target hash is calculated by subtracting the difficulty from 8 times the bytesize of the hash. For SHA-256, if there is a difficulty of 20, the target string is 256 - 20, or 236. 

    Hash (Object): 
    This is an object created that accepts bytes and subsequently hashes them into a string of encoded characters that cannot be reverse engineered into their original form. Hash Objects used in this program include the sha256 function object and the keccak_256 function object. A Scrypt function object is intended to be added at a later date. 

    Hash (String): 
    This is the string of encoded characters produced by a hashing function. This is what is output when printing the hash of a block. 

    Previous Hash: 
    This is the hash of the previous block. It is used for placement reference of the current block. 

    Block Number: 
    This is the index of the block in the blockchain. 

    Data: 
    This is the data of each block generated. This is made into a hash alongside the Timestamp, Previous Hash, Nonce and Block Number. 

    Timestamp: 
    This is the time in UTC that a hash is generated. If the hash is not accepted, the timestamp is reset with every new hash generated. 

    Head: 
    This is the first block in the blockchain. It is what is used to link to all other blocks in the blockchain. 

    Next: 
    This is the next block in reference to the current block of the blockchain. This is used to reference each block one after another. 

    Tail: 
    This is the last block in the blockchain. Its block number is used to reference the total amount of blocks in the block chain. Its next is none by default.

### Accepted Proof of Work Algorithms

In main.py there is a variable named pow, here are the accepted values for it to be used in the blockchain. 

    Any Variation of:

    ```
    keccak-256, keccak_256, or keccak 256
    ```
    ```
    scrypt
    ```
    Notice: A Scrypt hash function object is not currently included with the program. This is intended to be added at a later date. 

    Removal of the pow variable or assigning the variable an invalid value will cause the proof of work used to be the SHA-256 hashing algorithm by default.

## Authors

* **Andrew Wagner** - [GuiIsGooey](https://github.com/guiisgooey)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Sources

* [3Blue1Brown](https://www.youtube.com/watch?v=bBC-nXj3Ng4) for foundational knowledge on BlockChains and Cryptocurrencies. 
* [Bitcoin.it Wiki](https://en.bitcoin.it/) for insight into many of the processes of BlockChains and Cryptocurrencies
* [Python Docs](https://docs.python.org/3/library/hashlib.html) for explanations of the Sha-256 hash object
* [Pysha3 Module](https://pypi.org/project/pysha3/) for usage of sha3 for the Keccak-256 hash object