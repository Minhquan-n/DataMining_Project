import CreateApiService from './api.services'

class Services {
    constructor (baseURL = '/api') {
        this.api = CreateApiService(baseURL);
    }

    async bc_predict (data) {
        return (await this.api.post('/predict', data)).data;
    }

    
}

export default new Services;