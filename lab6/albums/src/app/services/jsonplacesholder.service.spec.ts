import { TestBed } from '@angular/core/testing';

import { JSONPlacesholderService } from './jsonplacesholder.service';

describe('JSONPlacesholderService', () => {
  let service: JSONPlacesholderService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(JSONPlacesholderService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
