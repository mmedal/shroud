import pytest

from shroud import encryption


@pytest.mark.incremental
class TestEncryption:

    def test_generate_rsa_key_pair(self):
        self.__class__.pub, self.__class__.priv = \
            encryption.generate_rsa_key_pair(passphrase='supersecret')

    def test_encrypt_secret_with_rsa_key(self):
        self.__class__.ciphertext = encryption.encrypt_secret_with_rsa_key(
            b'mysecret', self.__class__.pub)

    def test_decrypt_secret_with_rsa_key(self):
        assert encryption.decrypt_secret_with_rsa_key(
            self.__class__.ciphertext,
            private_key=self.__class__.priv,
            passphrase='supersecret'
        )  == b'mysecret'
