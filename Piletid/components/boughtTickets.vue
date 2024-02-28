<template>
    <!-- Card Section -->
<div class="">
  <!-- Grid -->
  <div class="grid sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-3 sm:gap-6">
    <!-- Card -->
    <a v-for="purchase in purchases" class="min-w-[15rem] group flex flex-col bg-white border shadow-sm rounded-xl hover:shadow-md transition dark:bg-slate-900 dark:border-gray-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">
      <div class="p-4 md:p-5">
        <div class="flex justify-between items-center">
          <div>
            <h3 class="group-hover:text-blue-600 font-semibold text-gray-800 dark:group-hover:text-gray-400 dark:text-gray-200">
              {{ purchase.ticket_id }}
            </h3>
          </div>
          <div class="ps-3">
            <svg class="flex-shrink-0 size-5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
          </div>
        </div>
      </div>
    </a>
    <!-- End Card -->  
  </div>
  <!-- End Grid -->
</div>
<!-- End Card Section -->
</template>

<script setup>
  const supabase = useSupabaseClient();
  const purchases = ref([]);
  const tickets = ref([]);

	async function getPurchases() {
		const { data } = await supabase
  			.from('purchases')
  			.select()
		purchases.value = data;
		console.log(purchases.value);
	}
  async function getTicketInfo() {
    const { data } = await supabase
      .from('tickets')
      .select()
    tickets.value = data;
    console.log(tickets.value);
  }

  onMounted(() => {
    getPurchases();
  });
</script>