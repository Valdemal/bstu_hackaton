export class TokenResponse {
    public auth_token : string;
    constructor(auth_token: string){
        this.auth_token = auth_token;
    }
}

export class Token {
    public self : string;
    constructor(self: string){
        this.self = self;
    }
}