<script>
    import Services from '../services/services';
    import AppHeader from '@/components/AppHeader.vue';

    export default {
        components: {
            AppHeader,
        },

        data() {
            return {
                patient_list: [],
                error_message: '',
                iserror: false,
                path: '',
                patient_list_state: 1,
                loading: false,
                empty_list: false,
            }
        },

        methods: {
            async get_patient_list () {
                this.loading = true;
                this.patient_list.length = 0;
                try {
                    const response = await Services.get_patient_list();
                    if (!response.error) {
                        this.patient_list = response.patient_list;
                        if (this.patient_list.length === 0) this.empty_list = true;
                        else this.empty_list = false;
                        this.patient_list_state = 1;
                        this.loading = false;
                    } else throw new Error(response.error)
                } catch (err) {
                    console.log(err)
                    this.error_message = 'Không thể tải danh sách bệnh nhân.';
                    this.iserror = true;
                    this.loading = false;
                    this.empty_list = true;
                }
            },

            async get_patient_list_non_predict () {
                this.loading = true;
                this.patient_list.length = 0;
                try {
                    const response = await Services.get_patient_list_nonpredict();
                    if (!response.error) {
                        this.patient_list = response.patient_list;
                        if (this.patient_list.length === 0) this.empty_list = true;
                        else this.empty_list = false;
                        this.patient_list_state = 2;
                        this.loading = false;
                    } else throw new Error(response.error)
                } catch (err) {
                    console.log(err)
                    this.error_message = 'Không thể tải danh sách bệnh nhân.';
                    this.iserror = true;
                    this.loading = false;
                    this.empty_list = true;
                }
            },

            async get_patient_list_recurrence () {
                this.loading = true;
                this.patient_list.length = 0;
                try {
                    const response = await Services.get_patient_list_recurrence();
                    if (!response.error) {
                        this.patient_list = response.patient_list;
                        if (this.patient_list.length === 0) this.empty_list = true;
                        else this.empty_list = false;
                        this.patient_list_state = 4;
                        this.loading = false;
                    } else throw new Error(response.error)
                } catch (err) {
                    console.log(err)
                    this.error_message = 'Không thể tải danh sách bệnh nhân.';
                    this.iserror = true;
                    this.loading = false;
                    this.empty_list = true;
                }
            },

            async get_patient_list_no_recurrence () {
                this.loading = true;
                this.patient_list.length = 0;
                try {
                    const response = await Services.get_patient_list_norecurrence();
                    if (!response.error) {
                        this.patient_list = response.patient_list;
                        if (this.patient_list.length === 0) this.empty_list = true;
                        else this.empty_list = false;
                        this.patient_list_state = 3;
                        this.loading = false;
                    } else throw new Error(response.error)
                } catch (err) {
                    console.log(err)
                    this.error_message = 'Không thể tải danh sách bệnh nhân.';
                    this.iserror = true;
                    this.loading = false;
                    this.empty_list = true;
                }
            },

            go_to_patient_detail_page (id) {
                console.log(id)
            }
        },

        created() {
            this.get_patient_list();
            this.path = window.location.pathname;
        }
    }
</script>

<template>
    <AppHeader/>
    <main>
        <div class="container p-2 m-2">
            <div class="row m-2 p-2">
                <ul class="nav nav-pills">
                    <li class="nav-item">
                        <router-link class="nav-link" :class="[(path.search('/') !== -1) ? 'active' : '']" aria-current="page" :to="{name: 'HomePage'}">Danh sách bệnh nhân</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :class="[(path.search('/patient') !== -1) ? 'active' : '']" :to="{name: 'AddPatientPage'}">Thêm bệnh nhân mới</router-link>
                    </li>
                </ul>
            </div>
            <div class="row m-2 p-2">
                <ul class="nav nav-pills w-100 d-flex justify-content-end align-items-center">
                    <li class="nav-item m-2">
                        <button 
                            class="btn btn-primary" 
                            :class="[patient_list_state === 1 ? 'active' : '']"
                            @click="get_patient_list"
                        >
                            Tất cả
                        </button>
                    </li>
                    <li class="nav-item m-2">
                        <button 
                            class="btn btn-primary" 
                            :class="[patient_list_state === 2 ? 'active' : '']"
                            @click="get_patient_list_non_predict"    
                        >
                                Chưa chuẩn đoán
                        </button>
                    </li>
                    <li class="nav-item m-2">
                        <button 
                            class="btn btn-primary" 
                            :class="[patient_list_state === 3 ? 'active' : '']"
                            @click="get_patient_list_no_recurrence"
                        >
                                Không tái phát
                        </button>
                    </li>
                    <li class="nav-item m-2">
                        <button 
                            class="btn btn-primary" 
                            :class="[patient_list_state === 4 ? 'active' : '']"
                            @click="get_patient_list_recurrence"
                        >
                                Tái phát
                        </button>
                    </li>
                </ul>
            </div>
            <div class="row">
                <div class="col p-3">
                    <div class="w-100 d-flex justify-content-center align-items-center" v-if="loading">
                        <div class="spinner-border" role="status" >
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                    <table class="table table-hover" v-else>
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <td scope="col">Họ tên</td>
                                <td scope="col">Tuổi</td>
                                <td scope="col">Địa chỉ</td>
                                <td scope="col">Chuẩn đoán</td>
                                <td scope="col"></td>
                            </tr>
                        </thead>
                        <tbody v-if="empty_list">
                            <tr>
                                <td colspan="5" class="text-center">Danh sách trống</td>
                            </tr>
                        </tbody>
                        <tbody v-else>
                            <tr v-for="item in patient_list" :key="item.patient_id">
                                <th scope="row">{{ item.patient_id }}</th>
                                <td>{{ item.patient_name }}</td>
                                <td>{{ item.current_age }}</td>
                                <td>{{ item.address }}</td>
                                <td v-if="item.prediction === null"> - </td>
                                <td v-else>{{ item.prediction }}</td>
                                <td>
                                    <button class="btn btn-primary">
                                        <router-link aria-current="page" :to="{name: 'PatientPage', params: {id: item.patient_id}}" style="color: white; text-decoration: none;">Xem chi tiết</router-link>
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </main>
</template>