import { createApp } from 'vue'
import './assets/main.css'
import App from './App.vue'
import router from './router'
import { FrappeUI } from 'frappe-ui'

const app = createApp(App)

app.use(router)
app.use(FrappeUI)

app.mount('#app')
