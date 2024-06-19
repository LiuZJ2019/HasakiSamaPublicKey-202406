## 说明

这是知乎@间宫羽咲sama的RSA公钥以及验证程序。即日起到2024年7月30日，我的所有文章内容都会附带一个内容一致的PDF版本，并在文章中注明该PDF的SHA-256值与SHA-256值的RSA签名。如果不具有这三者中的任意一条，均可视为不是我本人发布的。

如果同时具有这三条，则可以使用该程序校验PDF是否是我本人发布。校验方法为：

1. 安装python的Crypto库，如果你是Windows用户，可以使用 `pip install pycryptodome` 命令安装
2. 将我发布的PDF文件（如 `test.pdf` ）拷贝到本路径下
3. 将我发布的RSA签名替换掉第7行的 `signature` 变量内容（即 `b''` 内部的内容，保留 `b''` 这三个字符）
4. 运行程序，第一行输出为SHA-256值，应与我发布的SHA-256值一致。第二行输出 `Valid signature` 视为校验通过，说明是我本人发布的，否则说明不是我本人发布的。

测试用例：
1. 确保本目录下已存在 `hasaki-public-key.pem` ，这是我的RSA公钥（不用ECC的原因是配置折腾起来麻烦）
2. 本目录下 `test.pdf` 是测试样例
3. `test.pdf` 的SHA-256值是 `13539fe929cda06f093cb64335555cdc065a4f4881103af9e9ec92c57007bdc0`
4. `test.pdf` 的签名值（基于我的私钥，因此只有我能签名）是 `b'T/eHFZF3UXkBuEJ7LDfrnYyGRKquT3PffI86nrdJBpan1DNxCIPisBpuBk+Auy1nSzhyj0xlF84dlhN6TZe9ejftyqqZOx78snAb0eph8lSz/6kAPqxsAH32Czdgt+RnldXAchBUw/saijp12AuByY4pPsdqUmKURl6hFr9+4WJcbU9i1OGlobzTrEXMCHt8TWH4Mi+6kzEqXbevetaI5MrYaSMjSs6W8lLLYV2akKkUANgRhtxzha1/MBQ76bWUdjJOZPfUhkWGdN3joFdeoPpDvioN4Z7LwA/v4XW/k+OLOXpByu6EMfvBaT7+dkNbaZ4nF4f/ZXr4ULIhQvJqPw=='`
5. 运行，检查输出结果


