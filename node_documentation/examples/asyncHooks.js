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

// Allows callbacks of the asyncHook instance to call. This is not an implicit action
// after running the constructor, and must be run to execute callbacks
asyncHook.enable();

// The following callbacks can be passed to createHook()

// init is called during the object construction. The resource may not have
// completed construction when this callback runs, therefore all fields of the
// resource referenced by asyncId may not have been populated.
function init(asyncId, type, triggerAsyncId, resource){

}

// before is called just before the resource's callback is called. It can be
// called 0-N times for handles, and will be called exactly 1
// time for requests.
function before(asyncId) {

}

//after is called just after the resource's callback has finished
function after(asyncId) {

}

//destory is called when async wrap instance is destroyed
function destroy(asyncId) {

}

