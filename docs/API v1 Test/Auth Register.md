_________________________________
##### Documentation for Auth Rembang Smart City
_________________________________

### #REGISTER

```
    - Endpoint        : {HOST}/api/v1/auth/register
    - Methods         : POST
    - Content         : JSON
    - Login Required  : False
```

##### Body

```json
{
    "username":"test",
    "password":"test",
    "email":"test@gmail.com",
    "phone":"085",
    "name":"test"
}
```
##### Response <200>
```json
{
    "message":"register successfully",
    "status": "200"
}
```
##### Response <400>
    Bad Request

##### Response <409>
    Username/email is exist

#### Response <500>
    Internal Server Error

_____________________________________________
