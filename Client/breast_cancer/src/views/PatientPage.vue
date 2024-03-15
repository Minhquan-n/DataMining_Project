<script>
    import Services from '../services/services';
    import AppHeader from '@/components/AppHeader.vue';

    export default {
        components: {
            AppHeader,
        },

        data() {
            const patient_info = {
                id: 0,
                medical_record_id: 0,
                fullname: '',
                date_of_birth: '',
                current_age: 0,
                address: '',
                phone: '',
                prediction: '',
                age: "",
                menopause: "",
                tumor_size: "",
                inv_nodes: "",
                node_caps: "",
                deg_malig: 0,
                breast: "",
                breast_quad: "",
                irradiat: ""
            }

            return {
                patient_info,
                error_message: '',
                iserror: false,
                loading: false,
                ispredict: false,
                id_input: '',
            }
        },

        methods: {
            async get_prediction() {
                try {
                    this.ispredict = true;
                    const predict = await Services.predict(this.data);
                    if (predict) {
                        this.prediction = predict.prediction;
                    } else {
                        throw new Error('Fail');
                    }
                    this.ispredict = false;
                } catch (err){
                    console.log(err)
                    this.error_message = (err === 'Fail') ? 'Không thể dự đoán.' : 'Đã xảy ra lỗi.';
                    this.iserror = true;
                    this.ispredict = false;
                }
            },

            async get_patient_info(id) {
                try {
                    this.loading = true;
                    const response = await Services.get_patient_info(id);
                    if (response.patient_info.id == id) {
                        this.patient_info = response.patient_info;
                    } else {
                        throw new Error('Fail');
                    }
                    this.loading = false;
                } catch (err) {
                    console.log(err)
                    this.error_message = (err === 'Fail') ? 'Không thể tai' : 'Đã xảy ra lỗi.';
                    this.iserror = true;
                    this.loading = false
                }
            },
        },

        created() {
            this.id_input = this.$route.params.id
            this.get_patient_info(this.id_input);
        }
    }
</script>

<template>
    <AppHeader/>
    <main>
        <div class="container">
            <div class="row">
                <nav style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
                    <ol class="breadcrumb">
                        <li class="breadcrumb-item"><router-link :to="{name: 'HomePage'}">Danh sách bệnh nhân</router-link></li>
                        <li class="breadcrumb-item active" aria-current="page">{{ patient_info.fullname }}</li>
                    </ol>
                </nav>
            </div>
            <div class="row">
                <div class="col-3">
                    <div class="row text-center">
                        <h2>{{ patient_info.fullname }}</h2>
                    </div>
                    <div class="row">
                        <div class="info_field">
                            <b>Tuổi:</b>
                            <p>{{ patient_info.current_age }}</p>
                        </div>
                        <div class="info_field">
                            <b>Số điện thoại:</b>
                            <p>{{ patient_info.phone }}</p>
                        </div>
                        <div class="info_field">
                            <b>Địa chỉ:</b>
                            <p>{{ patient_info.address }}</p>
                        </div>
                    </div>
                </div>
                <div class="col-9">
                    <div class="row text-center">
                        <h2>Chỉ số</h2>
                    </div>
                    <div class="row">
                        <div class="col">
                            <div class="input-group mb-3">
                                <label class="input-group-text" for="inputGroupSelect01">Mãn kinh:</label>
                                <select class="form-select" id="inputGroupSelect01">
                                    <option selected>Dưới 40 tuổi</option>
                                    <option value="1">Trên 40 tuổi</option>
                                    <option value="2">Tiền mãn kinh</option>
                                </select>
                            </div>
                            <div class="input-group mb-3">
                                <label class="input-group-text" for="inputGroupSelect01">Kích thước khối u:</label>
                                <select class="form-select" id="inputGroupSelect01">
                                    <option selected>Dưới 40 tuổi</option>
                                    <option value="1">Trên 40 tuổi</option>
                                    <option value="2">Tiền mãn kinh</option>
                                </select>
                            </div>
                            <div class="input-group mb-3">
                                <label class="input-group-text" for="inputGroupSelect01">Hạch bạch huyết:</label>
                                <select class="form-select" id="inputGroupSelect01">
                                    <option selected>Dưới 40 tuổi</option>
                                    <option value="1">Trên 40 tuổi</option>
                                    <option value="2">Tiền mãn kinh</option>
                                </select>
                            </div>
                            <div class="input-group mb-3">
                                <label class="input-group-text" for="inputGroupSelect01">Di căn đến hạch bạch huyết:</label>
                                <select class="form-select" id="inputGroupSelect01">
                                    <option selected>Dưới 40 tuổi</option>
                                    <option value="1">Trên 40 tuổi</option>
                                    <option value="2">Tiền mãn kinh</option>
                                </select>
                            </div>
                            <div class="input-group mb-3">
                                <label class="input-group-text" for="inputGroupSelect01">Mức độ ác tính:</label>
                                <select class="form-select" id="inputGroupSelect01">
                                    <option selected>Dưới 40 tuổi</option>
                                    <option value="1">Trên 40 tuổi</option>
                                    <option value="2">Tiền mãn kinh</option>
                                </select>
                            </div>
                            <div class="input-group mb-3">
                                <label class="input-group-text" for="inputGroupSelect01">Vị trí vú:</label>
                                <select class="form-select" id="inputGroupSelect01">
                                    <option selected>Dưới 40 tuổi</option>
                                    <option value="1">Trên 40 tuổi</option>
                                    <option value="2">Tiền mãn kinh</option>
                                </select>
                            </div>
                            <div class="input-group mb-3">
                                <label class="input-group-text" for="inputGroupSelect01">Hướng vú:</label>
                                <select class="form-select" id="inputGroupSelect01">
                                    <option selected>Dưới 40 tuổi</option>
                                    <option value="1">Trên 40 tuổi</option>
                                    <option value="2">Tiền mãn kinh</option>
                                </select>
                            </div>
                            <div class="input-group mb-3">
                                <label class="input-group-text" for="inputGroupSelect01">Xạ trị:</label>
                                <select class="form-select" id="inputGroupSelect01">
                                    <option selected>Có</option>
                                    <option value="1">Không</option>
                                </select>
                            </div>
                        </div>
                        <div class="col">
                            <h3>Chuẩn đoán</h3>
                            <div class="input-group mb-3 col">
                                <select class="form-select" id="inputGroupSelect01">
                                    <option selected>U lành tính</option>
                                    <option value="1">U ác tính</option>
                                </select>
                            </div>
                            <div class="col">
                                <button class="btn btn-primary m-2">Lưu</button>
                                <button class="btn btn-primary m-2">Dự đoán</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>