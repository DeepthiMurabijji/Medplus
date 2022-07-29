import { TestBed } from '@angular/core/testing';

import { AuthjwtInterceptor } from './authjwt.interceptor';

describe('AuthjwtInterceptor', () => {
  beforeEach(() => TestBed.configureTestingModule({
    providers: [
      AuthjwtInterceptor
      ]
  }));

  it('should be created', () => {
    const interceptor: AuthjwtInterceptor = TestBed.inject(AuthjwtInterceptor);
    expect(interceptor).toBeTruthy();
  });
});
