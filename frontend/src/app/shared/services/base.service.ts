import {throwError as observableThrowError} from 'rxjs';
import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { BACKEND_HOST, BACKEND_PORT, BACKEND_PROTOCOL } from 'src/config';

export const SERVICE_URL = `${BACKEND_PROTOCOL}://${BACKEND_HOST}${BACKEND_PORT?':'+BACKEND_PORT:''}/api`; 
const CONTENT_TYPE_HEADER_KEY = 'Content-Type';
const CSRF_HEADER_KEY         = 'X-CSRFToken';

const CSRF_HEADER_VALUE = 'Wkw6zP87lbqCl7fATiDY1oEYzDMwXKa1k0SYBtjrB6n6vgmCqYGWv0i6ZQGx6FPn';

@Injectable()
export class BaseService {
  protected SERVICE_URL = SERVICE_URL;

  constructor(protected http: HttpClient) {}

  protected getHeaders(contentType: string = 'application/json'): HttpHeaders {
    let headers = new HttpHeaders();
        headers = headers.append(CONTENT_TYPE_HEADER_KEY, contentType);
        headers = headers.append(CSRF_HEADER_KEY, CSRF_HEADER_VALUE);
    return headers;
  }

  protected handleError(error: any) {
    let errMsg = error.message
      ? error.message
      : error.status
      ? `${error.status} - ${error.statusText}`
      : 'Server server-error';
    return observableThrowError(() => errMsg);
  }

  protected handleErrorStatus(error: any) {
    return observableThrowError(() => ({status: error.status, body: error.error}));
  }
}