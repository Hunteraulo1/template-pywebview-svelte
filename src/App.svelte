<script lang="ts">
  import { onMount } from 'svelte';
  import Header from './components/Header.svelte';
  import { apiService } from './lib/api.ts';

  let isLoading = true;
  let error: string | null = null;

  onMount(async () => {
    try {
      // Check API connection
      await apiService.healthCheck();
      isLoading = false;
    } catch (err) {
      error = 'Unable to connect to Python backend';
      isLoading = false;
    }
  });
</script>

<main class="max-w-6xl mx-auto p-5 font-sans">
  <Header />

  {#if isLoading}
    <div class="flex flex-col items-center justify-center min-h-96 gap-5">
      <div
        class="w-10 h-10 border-4 border-gray-200 border-t-primary-500 rounded-full animate-spin"
      ></div>
      <p class="text-gray-600">Loading application...</p>
    </div>
  {:else if error}
    <div
      class="text-center p-10 bg-red-50 border border-red-200 rounded-lg text-red-700"
    >
      <h2 class="text-xl font-semibold mb-2">Connection Error</h2>
      <p class="mb-4">{error}</p>
      <button
        class="px-5 py-2.5 bg-red-600 text-white border-0 rounded cursor-pointer hover:bg-red-700 transition-colors"
        onclick={() => window.location.reload()}
      >
        Retry
      </button>
    </div>
  {:else}
    <div>Application loaded successfully</div>
  {/if}
</main>
