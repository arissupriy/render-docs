_________________________________
##### Documentation for Auth Rembang Smart City
_________________________________

### #LOGIN

```
    - Endpoint        : {HOST}/api/v1/auth/login
    - Methods         : POST
    - Content         : JSON
    - Login Required  : False
```

#### Body

```json
{
    "username":"test",
    "password":"test"
}
```
#### Response <200>
```json
{
    "token":"jwt_token",
    "user":{
        "username":"",
        "xx":"xx",
        "yy":"yy"
    }
}
```
#### Response <400>
    Bad Request

#### Response <401>
    Login Failed

#### Response <500>
    Internal Server Error

_____________________________________________
