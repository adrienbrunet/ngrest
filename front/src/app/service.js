export default class AppService {
  constructor($http) {
    this.$http = $http;
  }

  getPeopleForm () {
    return this.$http({
      method: 'OPTIONS',
      url: '/api/peoples/'
    });
  }
}

