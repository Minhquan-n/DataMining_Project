import CreateApiService from './api.services'

class Services {
    constructor (baseURL = '/api') {
        this.api = CreateApiService(baseURL);
    }

    async predict (data) {
        return (await this.api.post('/predict', data)).data;
    }

    async get_patient_list () {
        return (await this.api.get('/patient')).data
    }

    async get_patient_list_nonpredict () {
        return (await this.api.get('/patient/nonpredict')).data
    }

    async get_patient_list_recurrence () {
        return (await this.api.get('/patient/recurrence')).data
    }

    async get_patient_list_norecurrence () {
        return (await this.api.get('/patient/norecurrence')).data
    }

    async get_patient_info (id) {
        return (await this.api.get(`/patient/${id}`)).data;
    }

    async create_patient (data) {
        return (await this.api.post('/patient', data)).data
    }
}

export default new Services;