package ecdsa

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"math/big"
)

type Key interface{
	Sign(payload []byte) (*big.Int, *big.Int, error)
	Kid() string
	JWKSJSON() ([]byte, error)
}

func LoadKey(d, x, y string) Key {
	dInt := new(big.Int)
	dInt.UnmarshalText([]byte(d))

	xInt := new(big.Int)
	xInt.UnmarshalText([]byte(x))

	yInt := new(big.Int)
	yInt.UnmarshalText([]byte(y))

	pkey := ecdsa.PrivateKey{
		D: dInt,
		PublicKey: ecdsa.PublicKey{
			Curve: elliptic.P256(),
			X: xInt,
			Y: yInt,
		},
	}

	return key{pkey: &pkey}
}

type key struct {
	pkey *ecdsa.PrivateKey
}

func (k key) Sign(payload []byte) (*big.Int, *big.Int, error) {
	return ecdsa.Sign(rand.Reader, k.pkey, payload)
}

func (k key) xtos() string {
	return base64.RawURLEncoding.EncodeToString(k.pkey.PublicKey.X.FillBytes(make([]byte, 32)))
}

func (k key) ytos() string {
	return base64.RawURLEncoding.EncodeToString(k.pkey.PublicKey.Y.FillBytes(make([]byte, 32)))
}

func (k key) Kid() string {
	jwkString := fmt.Sprintf(
		`{"crv":"P-256","kty":"EC","x":"%s","y":"%s"}`,
		k.xtos(),
		k.ytos(),
	)

	hash := make([]byte, 32)
	for i, b := range sha256.Sum256([]byte(jwkString)) { hash[i] = b }

	return base64.RawURLEncoding.EncodeToString(hash)
}

func (k key) JWKSJSON() ([]byte, error) {
	return json.Marshal(jwks{
		Keys: []jwk{
			{
				KeyType: "EC",
				KeyID: k.Kid(),
				Use: "sig",
				Algorithm: "ES256",
				Curve: "P-256",
				X: k.xtos(),
				Y: k.ytos(),
			},
		},
	})
}

type jwks struct {
	Keys []jwk `json:"keys"`
}

type jwk struct {
	KeyType string `json:"kty"`
	KeyID string `json:"kid"`
	Use string `json:"use"`
	Algorithm string `json:"alg"`
	Curve string `json:"crv"`
	X string `json:"x"`
	Y string `json:"y"`
}
