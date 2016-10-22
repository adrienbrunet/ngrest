import AppService from './service';

let validDefaultValue = (defaultValue) => (
  defaultValue !== '' &&
  defaultValue !== null &&
  angular.isDefined(defaultValue)
);


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

  getPeopleForm() {
    this.waitingPeopleForm = true;
    this.peopleFields = [];
    this.AppService.getPeopleForm().then(response => {

      let fields = response.data.actions.POST;

      // Convert defaultValue from string to date object for date inputs
      angular.forEach(fields, field => {
        if (
          (field.templateOptions.type === 'datetime-local' || field.templateOptions.type === 'date') &&
          validDefaultValue(field.defaultValue)
        ) {
          field.defaultValue = new Date(field.defaultValue);
        } else if (field.templateOptions.type === 'time' && validDefaultValue(field.defaultValue)) {
          let time = field.defaultValue.split(':');
          field.defaultValue = new Date(1970, 0, 1, Number(time[0]), Number(time[1]), Number(time[2]));
        }
      });

      this.peopleFields = fields;

    }).finally(() => {
      this.waitingPeopleForm = false;
    });
  }

  submitPeopleForm() {
    if (!this.people.pk) {
      this.AppService.createPeople(this.people).then(response => {
        console.log(response);
      });
    }
  }
}
