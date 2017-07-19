import rsa1 as r
import h
import numpy as np
import list_magic as lm

hill_key_e = None
hill_ordo_key = 0

def enter_key_hill():
    global hill_key_e
    global hill_ordo_key
    print("=====================================================")
    print("Hill Chipper memerlukan matriks persegi sebagai kunci")
    ordo = input("ordo matrix 'key': ")
    hill_ordo_key = int(ordo)
    key = []
    for row in range(hill_ordo_key):
        col_list = []
        col_text = input("| ")
        for col in col_text.split(" "):
            col_list.append(int(col))
        key.append(col_list)
    hill_key_e = np.array(key)
    print("\nKey:")
    print(hill_key_e)


def main():
    global hill_key_e
    global hill_ordo_key

    while True:
        print("\n"*3)
        print("=========================")
        print("    Hill Cipher + RSA")
        print("=========================\n")

        print("1. Enkripsi pesan")
        print("2. Dekripsi pesan")
        print("3. Goodbye")
        menu = input("pilih: ")
        if menu == "1":
            pesan = input("teks yang akan dienkripsi: ")
            p = 61
            q = 53
            print("p =", p)
            print("q =", q)
            enter_key_hill()
            import time
            start = time.time()
            (e, d, phi, n) = r.genkeys(p, q)
            print("public key =", e)
            print("private key =", d)
            print("n =", n)
            (n_hill, hill_key_d) = h.crypt(message=str(n), n=hill_ordo_key, cipher_matrix=hill_key_e)
            n2 = h.modhill(n, hill_ordo_key, hill_key_e)
            print("n * n_hill:", n2)
            pesan_e_num = r.encryptstr(e, n2, pesan)
            end = time.time()
            print("waktu: ", end-start)
            print("pesan terenkripsi:", pesan_e_num)

        elif menu == "2":
            encrypted_message = input("teks terenkripsi:")
            d = input("private key: ")
            n2 = input("n * n_hill : ")

            print("mendekripsi pesan...")
            print("pesan terenkripsi bentuk list: ", lm.int2list(int(encrypted_message)))
            pesan_d = r.decryptint(int(d), int(n2), int(encrypted_message))
            print("pesan terdekripsi:", pesan_d)

        elif menu == "3":
            exit()

        else:
            pass

if __name__ == "__main__":
    main()
