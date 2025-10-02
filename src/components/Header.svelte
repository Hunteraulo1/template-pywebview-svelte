<script lang="ts">
  import { onMount } from 'svelte';
  import { apiService } from '../lib/api';

  let healthStatus = 'Checking...';
  let lastCheck = '';

  onMount(async () => {
    await checkHealth();
    // Check API health every 30 seconds
    setInterval(checkHealth, 30000);
  });

  async function checkHealth() {
    try {
      const response = await apiService.healthCheck();
      healthStatus = 'Connected';
      lastCheck = new Date().toLocaleTimeString();
    } catch (error) {
      healthStatus = 'Disconnected';
      lastCheck = new Date().toLocaleTimeString();
    }
  }
</script>

<header class="bg-white shadow-lg mb-8 rounded-lg overflow-hidden">
  <div class="flex justify-between items-center p-6 flex-wrap gap-5">
    <div class="title-section">
      <h1 class="text-gray-800 text-3xl mb-1 font-bold">
        🚀 PyWebView + Svelte 5
      </h1>
      <p class="text-gray-600 text-base">
        Modern desktop application with Python and TypeScript
      </p>
    </div>

    <div class="flex flex-col items-end gap-1">
      <div
        class="flex items-center gap-2 px-4 py-2 rounded-full bg-gray-50 border-2 border-gray-200 transition-all duration-300"
        class:bg-green-50={healthStatus === 'Connected'}
        class:border-green-200={healthStatus === 'Connected'}
        class:text-green-800={healthStatus === 'Connected'}
      >
        <div
          class="w-2 h-2 rounded-full bg-gray-400 transition-all duration-300"
          class:bg-green-500={healthStatus === 'Connected'}
          class:animate-pulse={healthStatus === 'Connected'}
        ></div>
        <span class="text-sm font-medium">{healthStatus}</span>
      </div>
      {#if lastCheck}
        <small class="text-gray-500 text-xs"
          >Last check: {lastCheck}</small
        >
      {/if}
    </div>
  </div>
</header>
