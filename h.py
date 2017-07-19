import numpy as np
from collections import OrderedDict
a='the following functions are:'
b='(scrambled_message, key_matrix)=crypt(message,dimension(n), crypt_matrix (optional) ) for encrypting messages'
c='(unscrambled_message)=decrypt(scrambled_message, key_matrix) for decrypting messages'
d='(Inverted_modulo_matrix)=modinv(matrix,mod)'
# print(a)
# print(b)
# print(c)
# print(d)

def modhill(n, ordo,matrix):
    (n_hill, hill_key_d) = crypt(str(n), ordo, matrix)
    print("n terenkripsi hill cipher =",n_hill)
    print("n terenkripsi hill cipher % 3 =", int(n_hill) % 3)
    return int(n)*(int(n_hill) % 3)


def crypt(message='Hello World!', n=3, cipher_matrix=np.array([0])):
        #dictionary for keyboard characters
        a='0123456789'
        asciidict=OrderedDict(zip(a,range(0,10)))
        numbdict=OrderedDict(zip(range(0,10),a))
        msg=message

        #create message matrix
        msgL=list(msg)
        msgRValL=[asciidict[x] for x in msgL] #turn the msg list into ASCII characters
        msgsize=np.size(msgRValL)
        ncol=np.ceil(msgsize/n).astype(int)  #determine dimensions
        msgshape=(n,ncol)
        msgNA=np.resize(msgRValL,(msgshape)) # turn into matrix


        #create crypt matrix
        if np.array_equal(cipher_matrix, [0]):
                cipher_matrix=np.random.randint(0,10,(n,n))


        #create key
        A=cipher_matrix
        P=np.round(np.linalg.det(A)*np.linalg.inv(A))
        a=np.round(np.linalg.det(A))
        num=np.arange(1,10+1)
        res=np.mod(a*num, 10)
        b=np.where(res==1)
        err=np.size(b)
        if err == 0:
                print("The randomly generated cipher matrix is not modulable")
                return
        b=b[0].item(0)+1
        key_matrix=np.mod(b*P,10).astype(int)
        #find the inverse matrix (modulus 97)


        # print("cipher_matrix:\n",
            #   cipher_matrix)

        #scrambled matrix
        msgNAscr=np.mod(
                np.dot(cipher_matrix,msgNA),10
                )
        # print("Scrambled matrix:\n", msgNAscr)
        msgscr=list(np.concatenate(
                list(msgNAscr)
                ))
        scrambled_message=[numbdict[x] for x in msgscr]
        scrambled_message=''.join(scrambled_message)
        return (scrambled_message,key_matrix)


def decrypt(msg,key_matrix):
        a='0123456789'
        asciidict=OrderedDict(zip(a,range(0,10)))
        numbdict=OrderedDict(zip(range(0,10),a))

        #create message matrix
        msgL=list(msg)
        msgRValL=[asciidict[x] for x in msgL] #turn the msg list into ASCII characters
        msgsize=np.size(msgRValL)
        n=key_matrix.shape[0]
        ncol=np.ceil(msgsize/n).astype(int)
        msgshape=(n,ncol)
        msgDM=np.resize(msgRValL,(msgshape)) # turn into matrix

        #unscramble
        u_s=np.mod(
                np.dot(key_matrix,msgDM),10
                )
        u_s=list(np.concatenate(
                list(u_s)
                ))
        u_s=[numbdict[x] for x in u_s]
        unscrambled_message=''.join(u_s)
        return unscrambled_message

def modinv(matrix,modulo=10):
        #Inverted modulus matrix subroutine
        A=matrix
        m=modulo
        P=np.round(np.linalg.det(A)*np.linalg.inv(A))
        a=np.round(np.linalg.det(A))
        num=np.arange(1,m+1) #creates a modulo dictionary
        res=np.mod(a*num, m)
        b=np.where(res==1)
        err=np.size(b)
        if err == 0:
                print("The randomly generated cipher matrix is not modulable")
                return
        b=b[0].item(0)+1
        return np.mod(b*P,m).astype(int)
