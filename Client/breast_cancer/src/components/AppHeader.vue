<script>
    export default {
        data() {
            const nav_items = [
                {
                    id: 1,
                    path: '/dashboard',
                    routername: 'HomePage',
                    text: 'Trang chủ'
                },
                {
                    id: 2,
                    path: '/',
                    routername: 'HomePage',
                    text: 'Bệnh nhân'
                },
                {
                    id: 3,
                    path: '/celander',
                    routername: 'HomePage',
                    text: 'Lịch khám'
                },
                {
                    id: 4,
                    path: '/setting',
                    routername: 'HomePage',
                    text: 'Cài đặt'
                }
            ];

            return {
                nav_items,
                path: '',
            }
        },

        created () {
            this.path = window.location.pathname;
        }
    }
</script>

<template>
    <header>
        <router-link id="header_logo" :to="{name: 'HomePage'}"><h2>BREAST CANCER</h2></router-link>
        <div id="header_navigation">
            <ul class="nav w-100 p-2" :style="{display: open_nav === true ? 'flex' : ''}">
                <li class="nav-item w-100" v-for="item in nav_items" :key="item.id">
                    <router-link class="w-100 nav_item" :class="[(path.search(item.path) !== -1) ? 'nav_item_active' : '']" :to="{name: item.routername }">
                        {{ item.text }}
                    </router-link>
                </li>
            </ul>
        </div>
    </header>
</template>

<style>
    @import '@/assets/header.css';
</style>