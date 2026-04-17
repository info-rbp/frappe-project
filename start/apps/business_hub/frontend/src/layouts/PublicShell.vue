<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <!-- Announcement Bar -->
    <div class="bg-brand-900 text-white py-2 text-center text-xs font-medium tracking-wide">
      WELCOME TO THE UNIFIED BUSINESS PLATFORM
    </div>

    <!-- Main Header -->
    <header class="bg-white/80 backdrop-blur-md sticky top-0 z-50 border-b border-gray-100">
      <nav class="max-w-7xl mx-auto px-4 h-20 flex items-center justify-between">
        <!-- Brand -->
        <div class="flex items-center space-x-2">
          <div class="w-10 h-10 bg-brand-600 rounded-lg flex items-center justify-center text-white font-bold text-xl">
            B
          </div>
          <span class="text-xl font-bold tracking-tight text-gray-900">BusinessHub</span>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8">
          <router-link
            v-for="item in publicNavigation"
            :key="item.path"
            :to="item.path"
            class="text-sm font-medium text-gray-500 hover:text-brand-600 transition-colors"
            active-class="text-brand-600 font-semibold"
          >
            {{ item.name }}
          </router-link>
        </div>

        <!-- Auth Actions -->
        <div class="flex items-center space-x-4">
          <router-link to="/login" class="text-sm font-medium text-gray-600 hover:text-gray-900">
            Login
          </router-link>
          <router-link
            to="/join"
            class="bg-brand-600 text-white px-5 py-2.5 rounded-full text-sm font-semibold hover:bg-brand-700 transition-all shadow-sm active:scale-95"
          >
            Join Now
          </router-link>
        </div>
      </nav>
    </header>

    <!-- Main Content -->
    <main class="flex-grow">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-100 py-16">
      <div class="max-w-7xl mx-auto px-4 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-12">
        <div class="col-span-2 lg:col-span-1">
          <div class="flex items-center space-x-2 mb-6">
            <div class="w-8 h-8 bg-brand-600 rounded flex items-center justify-center text-white font-bold text-lg">
              B
            </div>
            <span class="text-lg font-bold tracking-tight">BusinessHub</span>
          </div>
          <p class="text-gray-500 text-sm leading-relaxed">
            The complete operating system for modern business managers and members.
          </p>
        </div>
        
        <div v-for="section in footerLinks" :key="section.title">
          <h4 class="font-bold text-gray-900 mb-6 uppercase text-xs tracking-widest">{{ section.title }}</h4>
          <ul class="space-y-4">
            <li v-for="link in section.links" :key="link.name">
              <router-link :to="link.path" class="text-sm text-gray-500 hover:text-brand-600 transition-colors">
                {{ link.name }}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
      
      <div class="max-w-7xl mx-auto px-4 mt-16 pt-8 border-t border-gray-50 flex flex-col md:flex-row justify-between items-center text-sm text-gray-400">
        <p>© 2026 Business Hub. All rights reserved.</p>
        <div class="flex space-x-6 mt-4 md:mt-0">
          <router-link to="/privacy">Privacy</router-link>
          <router-link to="/terms">Terms</router-link>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { publicNavigation } from '../config/navigation'

const footerLinks = [
  {
    title: 'Platform',
    links: [
      { name: 'Services', path: '/services' },
      { name: 'Membership', path: '/membership' },
      { name: 'Decision Desk', path: '/decision-desk' },
      { name: 'Tools', path: '/resources' },
    ]
  },
  {
    title: 'Resources',
    links: [
      { name: 'Documentation', path: '/documents' },
      { name: 'Templates', path: '/documents' },
      { name: 'Guides', path: '/help' },
    ]
  },
  {
    title: 'Company',
    links: [
      { name: 'About Us', path: '/about' },
      { name: 'Contact', path: '/contact' },
      { name: 'Support', path: '/help' },
    ]
  }
]
</script>
