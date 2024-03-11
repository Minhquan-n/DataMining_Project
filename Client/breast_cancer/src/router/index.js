import { createWebHistory, createRouter } from "vue-router";

const routes = [
    {
        path: '/patient',
        name: 'PatientPage',
        component: () => import('../views/PatientPage.vue'),
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;