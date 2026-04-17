<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script setup>
import { computed, defineAsyncComponent } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const layouts = {
  PublicShell: defineAsyncComponent(() => import('./layouts/PublicShell.vue')),
  AuthShell: defineAsyncComponent(() => import('./layouts/AuthShell.vue')),
  PortalShell: defineAsyncComponent(() => import('./layouts/PortalShell.vue')),
  AdminShell: defineAsyncComponent(() => import('./layouts/PortalShell.vue')),
}

const layout = computed(() => {
  return layouts[route.meta.layout] || layouts.PublicShell
})
</script>
