const asyncHooks = require('async_hooks');

// Return the ID of the current execution context
const eid = asyncHooks.executionAsyncId();
console.log(eid);

// Return the ID of the handle responsible for triggering the callback of the
// current execution scope to call
const tid = asyncHooks.triggerAsyncId();
console.log(tid);

// Create a new async hook instance. All of the callbacks are optional.
const asyncHook = asyncHooks.createHook({ init, before, after, destroy });
