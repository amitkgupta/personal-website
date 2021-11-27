package utils

import (
    "crypto/ecdsa"
    "crypto/elliptic"
    "crypto/rand"
    "math/big"
)

func GenerateKey() {
    pkey, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
    d, _ := pkey.D.MarshalText()
    x, _ := pkey.PublicKey.X.MarshalText()
    y, _ := pkey.PublicKey.Y.MarshalText()

    println(string(d), string(x), string(y))

    D := new(big.Int)
    D.UnmarshalText(d)

    X := new(big.Int)
    X.UnmarshalText(x)

    Y := new(big.Int)
    Y.UnmarshalText(y)

    PKEY := ecdsa.PrivateKey{
        D: D,
        PublicKey: ecdsa.PublicKey{
            Curve: elliptic.P256(),
            X: X,
            Y: Y,
        },
    }

    println(pkey.Equal(&PKEY))
}
