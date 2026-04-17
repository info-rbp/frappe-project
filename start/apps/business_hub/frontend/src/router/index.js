import { createRouter, createWebHistory } from 'vue-router'
import { routes as configRoutes } from '../config/navigation'
import PublicShell from '../layouts/PublicShell.vue'
import AuthShell from '../layouts/AuthShell.vue'
import PortalShell from '../layouts/PortalShell.vue'
import Placeholder from '../views/Placeholder.vue'

const layouts = {
  PublicShell: PublicShell,
  AuthShell: AuthShell,
  PortalShell: PortalShell,
  AdminShell: PortalShell, // Reusing Portal for Admin in blueprint phase
}

const routes = configRoutes.map((route) => ({
  path: route.path,
  name: route.name,
  component: Placeholder,
  meta: {
    layout: route.layout || 'PublicShell',
    title: route.name
  }
}))

// Use a parent route to handle multi-layout
const finalRoutes = [
  {
    path: '/',
    component: Object.values(layouts)[0], // Placeholder fallback
    children: routes
  }
]

// Better way: Flat routes with layout resolution in App.vue or via dynamic components
// For this blueprint, I'll use a simple approach: components resolve their own layout if needed, 
// but here I'll wrap the router-view in App.vue with a dynamic component.

export default createRouter({
  history: createWebHistory('/hub'),
  routes,
})
