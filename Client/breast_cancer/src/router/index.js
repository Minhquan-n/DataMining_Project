import { createWebHistory, createRouter } from "vue-router";

const routes = [
    {
        path: '/patient',
        name: 'AddPatientPage',
        component: () => import('../views/AddPatientPage.vue'),
    },

    {
        path: '/patient/:id',
        name: 'PatientPage',
        component: () => import('../views/PatientPage.vue'),
    },

    {
        path: '/',
        name: 'HomePage',
        component: () => import('../views/HomePage.vue'),
    },

    // Trang loi 404
    {
        path: '/:pathMatch(.*)*',
        name: 'PageNotFound',
        component: () => import('../views/PageNotFound.vue'),
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;