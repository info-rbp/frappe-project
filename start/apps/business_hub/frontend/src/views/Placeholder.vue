<template>
  <div class="py-20 px-4 text-center">
    <div class="max-w-2xl mx-auto bg-white p-12 rounded-2xl shadow-sm border border-gray-100">
      <h1 class="text-4xl font-bold text-gray-900 mb-4">{{ $route.name }}</h1>
      <p class="text-gray-500 text-lg mb-8">
        This is a shell placeholder for the <strong>{{ $route.meta.title }}</strong> route.
      </p>
      <div class="inline-flex items-center space-x-2 text-brand-600 font-medium">
        <span>Route: {{ $route.path }}</span>
      </div>
      <div class="mt-12 pt-8 border-t border-gray-50 text-sm text-gray-400">
        Implementation Shell - Phase 2
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
</script>
