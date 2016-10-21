export default class AppService {
  constructor($http) {
    this.$http = $http;
  }

  getPeopleForm () {
    return this.$http({
      method: 'OPTIONS',
      url: 'http://127.0.0.1:8000/api/peoples/',
      headers: {
        'Content-Type': 'application/json'
      },
    });
  }
}

