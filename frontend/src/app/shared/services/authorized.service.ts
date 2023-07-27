import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BaseService } from './base.service';
import { Token, TokenResponse } from '../models/token.models';

export const TOKEN_STORAGE_KEY = 'token';
const TOKEN_HEADER_KEY = 'Authorization';

@Injectable()
export class AuthorizedService extends BaseService{
  private token?: Token;
  
  constructor(protected override http: HttpClient) {
    super(http);
  }

  protected getTokenHeaders(contentType: string = 'application/json'): HttpHeaders {
    let token   = this.getToken;

    let headers = this.getHeaders(contentType);
        headers = headers.append(TOKEN_HEADER_KEY, `Token ${token}`);
    return headers;
  }

  private loadToken(){
    if (!this.token) {
      let tokenJSON = sessionStorage.getItem(TOKEN_STORAGE_KEY) ?? 'null';
      this.token    = JSON.parse(tokenJSON);
    }
  }

  protected get getToken(): string {
    this.loadToken();
    return this.token?.self ?? 'null';
  }

  protected get getTokenObj(): Token | undefined {
    this.loadToken();
    return this.token;
  }

  public setToken(tokenResp: TokenResponse) {
    this.token = new Token(tokenResp.auth_token);
    sessionStorage.setItem(TOKEN_STORAGE_KEY, JSON.stringify(this.token));
  }
}