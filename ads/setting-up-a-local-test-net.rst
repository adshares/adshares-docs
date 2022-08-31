
Setting up a local test net
==================================

Create a directory for your first node and the first user, and create link to key generator for convenience.

::

    mkdir /tmp/node1
    mkdir /tmp/user0
    ln -s `pwd`/external/ed25519/key /tmp/user0/key

To start the first node enter

::

    cd /tmp/node1
    echo 'svid=1' > options.cfg
    echo 'offi=9091' >> options.cfg
    echo 'port=8091' >> options.cfg
    adsd --init 1 -w .

The program will detect that it is in an empty directory and will create an initial setup
with a single node and an administrator account for the node.
You can stop a node by [Ctrl-C].
you can continue with the same block-chain by running the code again with the ``--init 1`` switch.

::

    adsd --init 1 -w .

The first node will start with the default node secret key stored in key/key.txt.
The secret key to the admin account is the same.
Secret keys can be created by running the key executable with a selected brain-key-string (ed25519/key "brain-key-string").
Both keys can be changed later.
In production the node key and the admin key should differ for security reasons.
To add more nodes and users open a new terminal and connect to the running node as admin (user with account number 0).
We have created a directory for the user previously.
Let's go there.

::

    cd /tmp/user0

Let's create the file containing the connection setting for the user.

::

    echo 'port=9091' > settings.cfg
    echo 'host=127.0.0.1' >> settings.cfg
    echo 'address=0001-00000000-XXXX' >> settings.cfg
    echo 'secret=14B183205CA661F589AD83809952A692DFA48F5D490B10FD120DA7BF10F2F4A0' >> settings.cfg
    chmod go-r settings.cfg

This is the account address of our user 0001-00000000-XXXX.
Last 4 characters should be hex characters defining the checksum.
They are optional and string "XXXX" can be provided instead.
Let's try to connect to the node and get the current status of our user.

::

    echo '{"run":"get_me"}' | ads -w . 2>err.txt

This command should list the current status of the user. We should get something like this:

.. code-block::

    {
        "current_block_time": "1534837760",
        "previous_block_time": "1534837248",
        "tx": {
            "data": "100100000000000100000000007AC47B5B",
            "signature": "CEC32B3484794BDBA19252C67C13F24600AEB0DF951E668BFB6DC5BAF7A9EAA2CA81C46F7DEA15BB4712EC06B6A190316628D46BB284EEDBAF7A09C13CDA780B",
            "time": "1534837882"
        },
        "account": {
            "address": "0001-00000000-9B6F",
            "node": "1",
            "id": "0",
            "msid": "1",
            "time": "1534837248",
            "date": "2018-08-21 09:40:48",
            "status": "0",
            "paired_node": "0",
            "paired_id": "0",
            "local_change": "1534837248",
            "remote_change": "1534837248",
            "balance": "38758205.99999999000",
            "public_key": "7D21F4EE7DE72EEDDC2EBFFEC5E7F33F140A975A629EE312075BB04610A9CFFF",
            "hash": "7FBDB0D6A217E5808B33363D13FC0B8E119EDAC625EA278197961B7DA429F5A5"
        },
        "network_account": {
            "address": "0001-00000000-9B6F",
            "node": "1",
            "id": "0",
            "msid": "1",
            "time": "1534837248",
            "date": "2018-08-21 09:40:48",
            "status": "0",
            "paired_node": "0",
            "paired_id": "0",
            "local_change": "1534837248",
            "remote_change": "1534837248",
            "balance": "38758205.99999999000",
            "public_key": "7D21F4EE7DE72EEDDC2EBFFEC5E7F33F140A975A629EE312075BB04610A9CFFF",
            "hash": "7FBDB0D6A217E5808B33363D13FC0B8E119EDAC625EA278197961B7DA429F5A5",
            "checksum": "true"
        }
    }

No standard output means the connection failed.
You can try to examine the err.txt file for some clues.
Correct standard output show the correct account number for the admin of the first node, which is "0001-00000000-9B6F"
(the checksum is "9B6F").
Now let's change our secret key and create a new account with a new key. First let's generate 2 keys.

::

    ./key "user-0-0"

::

    SK: FF767FC8FAF9CFA8D2C3BD193663E8B8CAC85005AD56E085FAB179B52BD88DD6
    PK: D69BCCF69C2D0F6CED025A05FA7F3BA687D1603AC1C8D9752209AC2BBF2C4D17
    SG: 7A1CA8AF3246222C2E06D2ADE525A693FD81A2683B8A8788C32B7763DF6037A5DF3105B92FEF398AF1CDE0B92F18FE68DEF301E4BF7DB0ABC0AEA6BE24969006

::

    ./key "user-0-1"

::

    SK: 5BF11F5D0130EC994F04B6C5321566A853B7393C33F12E162A6D765ADCCCB45C
    PK: C9965A1417F52B22514559B7608E4E2C1238FCA3602382C535D42D1759A2F196
    SG: ED8479C0EDA3BB02B5B355E05F66F8161811F5AD9AE9473AA91E2DA32457EAB850BC6A04D6D4D5DDFAB4B192D2516D266A38CEA4251B16ABA1DF1B91558A4A05

The secret keys are printed in the lines starting with "SK:".
The line starting with "SG:" contains the signature of an empty phrase signed with the secret key.
This signature is used as checksum when creating a new account.
Let's change the key for the admin account now:

::

    (echo '{"run":"get_me"}';echo '{"run":"change_account_key","public_key":"D69BCCF69C2D0F6CED025A05FA7F3BA687D1603AC1C8D9752209AC2BBF2C4D17","confirm":"7A1CA8AF3246222C2E06D2ADE525A693FD81A2683B8A8788C32B7763DF6037A5DF3105B92FEF398AF1CDE0B92F18FE68DEF301E4BF7DB0ABC0AEA6BE24969006"}') | ads -w.

In response should be ``PKEY changed`` result.
After this the admin needs a new secret key to connect to its account, so let's fix the settings.cfg file.

::

    echo 'port=9091' > settings.cfg
    echo 'host=127.0.0.1' >> settings.cfg
    echo 'address=0001-00000000-9B6F' >> settings.cfg
    echo 'secret= FF767FC8FAF9CFA8D2C3BD193663E8B8CAC85005AD56E085FAB179B52BD88DD6' >> settings.cfg

And confirm that we can connect again with the new key.

::

    echo '{"run":"get_me"}' | ads -w . 2>err.txt

The output should indicate that our transaction id was incremented and is now equal 2 ("msid": "2",).
Let's now create the second user.

::

    (echo '{"run":"get_me"}'; echo '{"run":"create_account"}') | ads -w .

The new user is managed by our node so the creation process will be fast
and the node will report the new account number for the local user in the paired_id field ("paired_id": "1").
Let's read the status of the new user account.

::

    echo '{"run":"get_account","address":"0001-00000001-XXXX"}' | ads -w .

We should see that the correct new account address is "0001-00000001-8B4E".
The balance of the new user is too small to make any transactions so let's send him some funds.

::

    (echo '{"run":"get_me"}'; echo '{"run":"send_one","address":"0001-00000001-8B4E","amount":0.1,"message":"000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F"}') | ads -w .

The new balance should be 0.10020000000

::

    echo '{"run":"get_account","address":"0001-00000001-8B4E"}' | ads -w . 2>/dev/null | grep balance

Let's change the public key of the new user by connecting as the new user with the current copied key.
Do not forget to use the ``--address 0001-00000001-8B4E`` here, otherwise you will change your own public key.
In normal cases you don't know the corresponding secret key so you will loose your account.

::

    (echo '{"run":"get_me"}'; echo '{"run":"change_account_key","public_key":"C9965A1417F52B22514559B7608E4E2C1238FCA3602382C535D42D1759A2F196","confirm":"ED8479C0EDA3BB02B5B355E05F66F8161811F5AD9AE9473AA91E2DA32457EAB850BC6A04D6D4D5DDFAB4B192D2516D266A38CEA4251B16ABA1DF1B91558A4A05"}' ) | ads -w . --address 0001-00000001-8B4E

The output should indicate that the public key was changed.
Let's connect as the new user after setting up the new environment.

::

    mkdir ../user1
    cd ../user1
    echo 'port=9091' > settings.cfg
    echo 'host=127.0.0.1' >> settings.cfg
    echo 'address=0001-00000001-8B4E ' >> settings.cfg
    echo 'secret= 5BF11F5D0130EC994F04B6C5321566A853B7393C33F12E162A6D765ADCCCB45C ' >> settings.cfg
    chmod go-r settings.cfg
    echo '{"run":"get_me"}' | ads -w .

The output should indicate that you have successfully connected to the node as user "0001-00000001-8B4E".
You don't have enough funds to create a new node.
User0 will help you.

::

    cd ../user0
    (echo '{"run":"get_me"}'; echo '{"run":"send_one","address":"0001-00000001-8B4E","amount":10000,"message":"000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F"}') | ads -w .

Let's now try to create a new node.
The new node will get the public key of the requesting user.

::

    cd ../user1
    (echo '{"run":"get_me"}'; echo '{"run":"create_node"}') | ads -w .

It will take at least 1 block time for the network to create a new node.
You can examine the log of the first node.
Before block creation the node should show now info about 3 nodes (the first one is the unused node number 0).
You should see lines like these

::

    NOD: 00000000 00000000 ffff0000 00000000 595E8D80 0 0000000000000000 0
    NOD: eef4217d c08c88e1 8936fa16 0000003C 595EA5BB 6 3FFFC1DB71A5379A 2
    NOD: 145a96c9 e186f4ad ffff0002 00000000 595EA5A0 0 0000000FFFF08000 1

When the new node is created, you can send some funds to the new admin account (0002-00000000-XXXX) if you plan to perform any transaction.
We will skip it because we will only try to connect a new node.

Let's create the directory and the files for the new node

::

    mkdir ../node2
    cd ../node2
    echo 'svid=2' > options.cfg
    echo 'offi=9092' >> options.cfg
    echo 'port=8092' >> options.cfg
    echo 'addr=127.0.0.1' >> options.cfg
    echo 'peer=127.0.0.1:8091' >> options.cfg
    mkdir key
    chmod go-rx key/
    echo '5BF11F5D0130EC994F04B6C5321566A853B7393C33F12E162A6D765ADCCCB45C' > key/key.txt
    chmod go-r key/key.txt

The configuration file (options.cfg) indicates an initial peer address that we want to start syncing from.
Now we should be able to connect the new node to the network.

::

    adsd -f 1 -w .

The connection should be established shortly.
You can stop the node again by [Ctrl-C].
The -f switch indicates that we want to start from the current status of the blockchain.
After stopping the second node, we should start it again without the -f option to load the missing blocks.

::

    adsd -w .

Connecting more nodes can be done iteratively.
The nodes broadcast their IPs and ports on the network,
so there is no need to provide many peers in the options.cfg file.
