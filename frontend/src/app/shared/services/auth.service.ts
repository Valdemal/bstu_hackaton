import { HttpClient } from "@angular/common/http";
import { AuthorizedService } from "./authorized.service";
import { Observable, catchError } from "rxjs";
import { Injectable } from "@angular/core";
import { TokenResponse } from "../models/token.models";
import { AuthData } from "../models/auth-data.model";

@Injectable()
export class AuthService extends AuthorizedService {
    private CONTROLLER_NAME = 'auth';
    private CONTROLLER_URL  = `${this.SERVICE_URL}/${this.CONTROLLER_NAME}`;

    constructor(http: HttpClient){
        super(http);
    }

    public authorize(username: string, password: string): Observable<TokenResponse>{
        let url     = `${this.CONTROLLER_URL}/token/login/`;
        let body    = new AuthData(username, password);
        let headers = this.getHeaders();
        let options = {headers: headers};
        return this.http.post<TokenResponse>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public logout(): Observable<void>{
        let url     = `${this.CONTROLLER_URL}/token/logout/`;
        let body    = {};
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<void>(url, body, options)
            .pipe(catchError(this.handleError));
    }

}