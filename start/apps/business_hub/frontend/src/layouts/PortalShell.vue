<template>
  <div class="h-screen flex bg-white overflow-hidden">
    <!-- Sidebar -->
    <div class="hidden md:flex md:flex-shrink-0">
      <div class="flex flex-col w-64 border-r border-gray-100 bg-gray-50/50">
        <div class="flex flex-col flex-grow pt-5 pb-4 overflow-y-auto">
          <div class="flex items-center flex-shrink-0 px-4 space-x-2">
             <div class="w-8 h-8 bg-brand-600 rounded flex items-center justify-center text-white font-bold text-lg">
              B
            </div>
            <span class="text-lg font-bold tracking-tight">BusinessHub</span>
          </div>
          <div class="mt-8 flex-1 flex flex-col">
            <nav class="flex-1 px-4 space-y-1">
              <router-link
                v-for="item in portalLinks"
                :key="item.path"
                :to="item.path"
                class="group flex items-center px-3 py-2 text-sm font-medium rounded-lg transition-colors"
                active-class="bg-brand-50 text-brand-700"
                class-inactive="text-gray-500 hover:bg-gray-100"
              >
                {{ item.name }}
              </router-link>
            </nav>
          </div>
        </div>
        <div class="flex-shrink-0 flex border-t border-gray-100 p-4">
          <div class="flex items-center space-x-3">
            <div class="w-9 h-9 rounded-full bg-brand-100 flex items-center justify-center text-brand-700 font-bold">
              JD
            </div>
            <div class="text-sm">
              <p class="font-medium text-gray-900">John Doe</p>
              <p class="text-xs text-gray-500">Member</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="flex flex-col w-0 flex-1 overflow-hidden">
      <header class="bg-white border-b border-gray-100 md:hidden">
        <!-- Mobile Header placeholder -->
      </header>
      <main class="flex-1 relative overflow-y-auto focus:outline-none">
        <div class="py-6 h-full">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8 h-full">
            <router-view />
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
const portalLinks = [
  { name: 'Dashboard', path: '/portal/dashboard' },
  { name: 'Membership', path: '/portal/membership' },
  { name: 'Resources', path: '/portal/resources' },
  { name: 'Finance', path: '/portal/finance' },
  { name: 'Account', path: '/portal/account' },
]
</script>
