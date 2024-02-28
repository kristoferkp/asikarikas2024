<template>
	<div class="max-w-6xl py-10 px-4 sm:px-6 lg:px-8 lg:py-16 mx-auto">
		<div class="max-w-xl text-center mx-auto">
			<div class="mb-5">
				<h2
					class="text-2xl font-bold md:text-3xl md:leading-tight dark:text-white">
					Osta pilet
				</h2>
			</div>

			<form @submit.prevent="findTicket">
				<div
					class="mt-5 lg:mt-8 flex flex-col items-center gap-2 sm:flex-row sm:gap-3">
					<div class="w-full">
						<input
							type="text"
							id="to_city"
							name="to_city"
							class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
							placeholder="Lisa sihtkoht" />
					</div>
					<div class="w-full">
						<input
							type="text"
							id="from_city"
							name="from_city"
							class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
							placeholder="Lisa lähtekoht" />
					</div>
					<input
						type="submit"
						:value="loading ? 'Laeb' : 'Leia pilet'"
						:disabled="loading"
						class="max-w-sm py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-gradient-to-tl from-blue-600 to-violet-600 hover:from-violet-600 hover:to-blue-600 text-white disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" />
				</div>
			</form>
		</div>
	</div>
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
									<th scope="col" class="px-6 py-3 text-start">
										<span
											class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											
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
									<td class="h-px w-auto whitespace-nowrap">
										<button @click="buy(ticket)" class="max-w-sm m-1 py-2 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-gradient-to-tl from-blue-600 to-violet-600 hover:from-violet-600 hover:to-blue-600 text-white disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" >
											Osta
										</button>
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

<script setup>
	const supabase = useSupabaseClient();
	const tickets = ref([]);
	const loading = ref(false);

	async function getTickets(userInputFromCity, userInputToCity) {
		const { data } = await supabase
  			.from('tickets')
  			.select()
  			.eq('from', userInputFromCity)
  			.eq('to', userInputToCity);
		tickets.value = data;
		console.log(tickets.value);
	}
	
	async function findTicket(event) {
		event.preventDefault();
		const to_city = document.getElementById("to_city").value;
		const from_city = document.getElementById("from_city").value;
		const { data, error } = await supabase
			.from("tickets")
			.select("*")
			.eq("to", to_city)
			.eq("from", from_city);
		if (error) {
			alert('Viga pileti leidmisel');
		} else if (data.length === 0) {
			alert(`Ei leitud midagi sihtkohaga ${to_city} ja lähtekohaga ${from_city}`);
		} else {
			getTickets(to_city, from_city);
		}
	}
	async function buy(ticket) {
		const user = supabase.auth.getUser();
		console.log(ticket);
		if (!user) {
			alert('Logi sisse, et osta pilet');
			return;
		}
		const { data, error } = await supabase
			.from("purchases")
			.insert([
				{
					ticket_id: ticket.ticket_id,
				},
			]);
		if (error) {
			alert('Viga pileti ostmisel');
		} else {
			const email = user.email
			const { data, error } = await supabase.auth.resetPasswordForEmail(user.email, {
				redirectTo: '/kasutaja',
			})
		}
	}
</script>
