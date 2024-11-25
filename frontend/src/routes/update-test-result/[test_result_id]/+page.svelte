<script lang="ts">
    import { onMount } from "svelte";
    import TestResultForm from "../../../components/test-result-form.svelte";
    import TestResultEntityInstance from "$lib/entities/test-results";
    import { page } from "$app/stores";
    import type { TestResult } from "$lib/entities/test-results";

    let testResult: TestResult | null = $state(null);
    onMount(() => {
        const sub = page.subscribe(async (value) => {
            const { test_result_id } = value.params;

            testResult = await TestResultEntityInstance.get(
                Number(test_result_id),
            );
        });

        sub();
    });
</script>

{#if testResult}
    <TestResultForm form={testResult} testResultId={testResult.id}
    ></TestResultForm>
{/if}
