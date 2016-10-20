import AppService from './service';


export default class AppCtrl {
  constructor(AppService) {
    this.title = 'ng-rest-form test';
    this.people = {};
    this.waitingPeopleForm = false;

    // note, these field types will need to be
    // pre-defined. See the pre-built and custom templates
    // http://docs.angular-formly.com/v6.4.0/docs/custom-templates
    this.peopleFields = [
      {
        key: 'email',
        type: 'input',
        templateOptions: {
          type: 'email',
          label: 'Email address',
          placeholder: 'Enter email'
        }
      },
      {
        key: 'password',
        type: 'input',
        templateOptions: {
          type: 'password',
          label: 'Password',
          placeholder: 'Password'
        }
      },
      {
        key: 'checked',
        type: 'checkbox',
        templateOptions: {
          label: 'Check me out'
        }
      }
    ];

    this.AppService = AppService;
  }

  getPeopleForm(){
    this.AppService.getPeopleForm().then(response => {
      console.log(response);
      this.peopleFields = response;
    }).finally(() => {
      self.waitingPeopleForm = false;
    });
  }
}
