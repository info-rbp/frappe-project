<template>
  <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md text-center">
      <div class="inline-flex items-center justify-center w-16 h-16 bg-brand-600 rounded-2xl text-white text-3xl font-bold mb-6">
        B
      </div>
      <h2 class="text-3xl font-extrabold text-gray-900 tracking-tight">
        {{ $route.name }}
      </h2>
      <p class="mt-2 text-sm text-gray-500">
        Unified Business Platform
      </p>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow-xl shadow-brand-900/5 rounded-2xl sm:px-10 border border-gray-100">
        <router-view />
      </div>
      
      <div class="mt-6 text-center">
        <router-link to="/" class="text-sm font-medium text-gray-400 hover:text-brand-600 transition-colors">
          &larr; Back to website
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
// Auth Shell Template
</script>
