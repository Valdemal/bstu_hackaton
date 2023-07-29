import { HttpClient } from "@angular/common/http";
import { AuthorizedService } from "./authorized.service";
import { Observable, catchError } from "rxjs";
import { User } from "../models/user.model";
import { ActivationModel } from "../models/activation.model";
import { EmailRequest, PasswordRequest, PasswordResetRequest, UsernameRequest, UsernameResetRequest } from "../models/requests.models";
import { Injectable } from "@angular/core";

@Injectable()
export class UsersService extends AuthorizedService {
    private CONTROLLER_NAME = 'users';
    private CONTROLLER_URL  = `${this.SERVICE_URL}/${this.CONTROLLER_NAME}`;

    constructor(http: HttpClient){
        super(http);
    }

    public getUsersList() : Observable<User[]> {
        let url     = this.CONTROLLER_URL;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.get<User[]>(url, options)
            .pipe(catchError(this.handleError));
    }

    public createUser(user: User) : Observable<User>{
        let url     = this.CONTROLLER_URL;
        let body    = user;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<User>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public activateUser(model: ActivationModel) : Observable<ActivationModel> {
        let url     = `${this.CONTROLLER_URL}/activation/`;
        let body    = model;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<ActivationModel>(url, body, options)
            .pipe(catchError(this.handleError));
    }

    public getSelfUser() : Observable<User> {
        let url     = `${this.CONTROLLER_URL}/me/`;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.get<User>(url, options)
            .pipe(catchError(this.handleError));
    }
    public redactSelfUser(user: User) : Observable<User> {
        let url     = `${this.CONTROLLER_URL}/me/`;
        let body    = user;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.put<User>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public patchSelfUser(user: User) : Observable<User> {
        let url     = `${this.CONTROLLER_URL}/me/`;
        let body    = user;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.patch<User>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public deleteSelfUser() : Observable<void> {
        let url     = `${this.CONTROLLER_URL}/me/`;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.delete<void>(url, options)
            .pipe(catchError(this.handleError));
    }

    public resendActivation(email: string) : Observable<EmailRequest> {
        let url     = `${this.CONTROLLER_URL}/resend_activation/`;
        let body    = new EmailRequest(email);
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<EmailRequest>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public resetPassword(email: string) : Observable<EmailRequest> {
        let url     = `${this.CONTROLLER_URL}/reset_password/`;
        let body    = new EmailRequest(email);
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<EmailRequest>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public confirmPasswordReset(model: PasswordResetRequest) : Observable<PasswordResetRequest> {
        let url     = `${this.CONTROLLER_URL}/reset_password_confirm/`;
        let body    = model;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<PasswordResetRequest>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public resetUsername(email: string) : Observable<EmailRequest> {
        let url     = `${this.CONTROLLER_URL}/reset_username/`;
        let body    = new EmailRequest(email);
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<EmailRequest>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public confirmUsernameReset(newUsername: string) : Observable<UsernameResetRequest> {
        let url     = `${this.CONTROLLER_URL}/reset_username_confirm/`;
        let body    = new UsernameResetRequest(newUsername);
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<UsernameResetRequest>(url, body, options)
            .pipe(catchError(this.handleError));
    }

    public setPassword(currentPassword: string, newPassword: string) : Observable<PasswordRequest> {
        let url     = `${this.CONTROLLER_URL}/set_password/`;
        let body    = new PasswordRequest(currentPassword, newPassword);
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<PasswordRequest>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public setUsername(currentPassword: string, newUsername: string) : Observable<void> {
        let url     = `${this.CONTROLLER_URL}/set_username/`;
        let body    = new UsernameRequest(currentPassword, newUsername);
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.post<void>(url, body, options)
            .pipe(catchError(this.handleError));
    }


    public getUser(id: number) : Observable<User> {
        let url     = `${this.CONTROLLER_URL}/${id}/`;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.get<User>(url, options)
            .pipe(catchError(this.handleError));
    }
    public redactUser(id: number, user: User) : Observable<User> {
        let url     = `${this.CONTROLLER_URL}/${id}/`;
        let body    = user;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.put<User>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public patchUser(id: number, user: User) : Observable<User> {
        let url     = `${this.CONTROLLER_URL}/${id}/`;
        let body    = user;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.patch<User>(url, body, options)
            .pipe(catchError(this.handleError));
    }
    public deleteUser(id: number) : Observable<void> {
        let url     = `${this.CONTROLLER_URL}/${id}/`;
        let headers = this.getTokenHeaders();
        let options = {headers: headers};
        return this.http.delete<void>(url, options)
            .pipe(catchError(this.handleError));
    }
}