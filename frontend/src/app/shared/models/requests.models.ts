export class EmailRequest{
    public email : string;
    constructor(email: string){
        this.email = email;
    }
}

export class PasswordResetRequest{
    public uid          : string ;
    public token        : string ;
    public new_password : string ;
    constructor(uid: string, token: string, new_password: string){
        this.uid          = uid          ;
        this.token        = token        ;
        this.new_password = new_password ;
    }
}

export class UsernameResetRequest{
    public new_username : string;
    constructor(new_username: string){
        this.new_username = new_username;
    }
}

export class UsernameRequest{
    public current_password : string;
    public new_username     : string;
    constructor(current_password: string, new_username: string){
        this.current_password = current_password ;
        this.new_username     = new_username     ;
    }
}

export class PasswordRequest{
    public current_password : string;
    public new_password     : string;
    constructor(current_password: string, new_username: string){
        this.current_password = current_password ;
        this.new_password     = new_username     ;
    }
}