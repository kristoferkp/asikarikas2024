<script setup>
	const supabase = useSupabaseClient();

	async function getTickets(userInputFromCity, userInputToCity) {
		const tickets = ref([]);
		const { data } = await supabase
  			.from('tickets')
  			.select()
  			.eq('from', userInputFromCity)
  			.eq('to', userInputToCity);
		tickets.value = data;
		console.log(tickets.value);

	
	}
</script>

<template>
	<!-- Table Section -->
	<div class="max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
		<!-- Card -->
		<div class="flex flex-col">
			<div class="-m-1.5 overflow-x-auto">
				<div class="p-1.5 min-w-full inline-block align-middle">
					<div
						class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden dark:bg-slate-900 dark:border-gray-700">
						<!-- Header -->
						<div
							class="px-6 py-4 grid gap-3 md:flex md:justify-between md:items-center border-b border-gray-200 dark:border-gray-700">
							<div>
								<h2
									class="text-xl font-semibold text-gray-800 dark:text-gray-200">
									Piletid
								</h2>
							</div>
						</div>
						<!-- End Header -->

						<!-- Table -->
						<table
							class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
							<thead
								class="bg-gray-50 divide-y divide-gray-200 dark:bg-gray-800 dark:divide-gray-700">
								<tr>
									<th scope="col" class="px-6 py-3 text-start">
										<span
											class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											Lähtepeatus
										</span>
									</th>
									<th scope="col" class="px-6 py-3 text-start">
										<span
											class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											Sihtpeatus
										</span>
									</th>
									<th scope="col" class="px-6 py-3 text-start">
										<span
											class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											Stardi aeg
										</span>
									</th>

									<th scope="col" class="px-6 py-3 text-start">
										<span
											class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											Kohalejõudmise aeg
										</span>
									</th>

									<th scope="col" class="px-6 py-3 text-start">
										<span
											class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											Kuupäev
										</span>
									</th>

									<th scope="col" class="px-6 py-3 text-start">
										<span
											class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											Transpordivahend
										</span>
									</th>

									<th scope="col" class="px-6 py-3 text-start">
										<span
											class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											Hind
										</span>
									</th>
								</tr>
							</thead>

							<tbody class="divide-y divide-gray-200 dark:divide-gray-700">
								<tr v-for="ticket in tickets">
									<td class="h-px w-auto whitespace-nowrap">
										<div class="px-6 py-2 flex items-center gap-x-3">
											<span class="text-sm text-gray-600 dark:text-gray-400">
                                                {{ ticket.from }}
                                            </span>
										</div>
									</td>
									<td class="h-px w-auto whitespace-nowrap">
										<div class="px-6 py-2 flex items-center gap-x-3">
											<span class="font-semibold text-sm text-gray-600 dark:text-gray-400">
                                                {{ ticket.to }}
                                            </span>
										</div>
									</td>
									<td class="h-px w-auto whitespace-nowrap">
										<div class="px-6 py-2 flex items-center gap-x-3">
											<span class="font-semibold text-sm text-gray-600 dark:text-gray-400">
                                                {{ ticket.start_time }}
                                            </span>
										</div>
									</td>
									<td class="h-px w-auto whitespace-nowrap">
										<div class="px-6 py-2">
											<span
												class="text-sm text-gray-800 dark:text-gray-200"
												>{{ ticket.end_time }}</span
											>
										</div>
									</td>
									<td class="h-px w-auto whitespace-nowrap">
										<div class="px-6 py-2 flex items-center gap-x-3">
											<span class="text-sm text-gray-600 dark:text-gray-400">
                                                {{ ticket.date }}
                                            </span>
										</div>
									</td>
									<td class="h-px w-auto whitespace-nowrap">
										<div class="px-6 py-2">
											<span class="text-sm text-gray-800 dark:text-gray-200"
												>{{ ticket.vehicle_type }}</span
											>
											
										</div>
									</td>
									<td class="h-px w-auto whitespace-nowrap">
										<div class="px-6 py-2">
											<span class="font-semibold text-sm text-gray-800 dark:text-gray-200"
												>{{ ticket.price }}€</span
											>
										</div>
									</td>
									
								</tr>
							</tbody>
						</table>
						<!-- End Table -->

						
					</div>
				</div>
			</div>
		</div>
		<!-- End Card -->
	</div>
	<!-- End Table Section -->
</template>
