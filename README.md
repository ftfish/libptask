# libptask

Libptask is a pure C99 parallel task execution library on pthread. A set of worker threads are created for each call of the `ptask_init` function. Tasks are distributed to the threads in a simple, one-shot parallel manner with `ptask_parallel` or streaming, scatter-and-gather manner with `ptask_stream`. The library internally uses [a pthread-based queue implementation by tobithiel](https://github.com/tobithiel/Queue). The library is developed as a submodule of the comb aligner.

## Build

Python (2.7 or 3.x) is required to run the build script written in [waf](https://github.com/waf-project/waf).

```
$ ./waf configure
$ ./waf build
```

## Functions


### ptask_init

Create worker threads and queues and returns a pointer to the context. The `worker` function will be called with `worker_arg[thread_id]` thus worker_arg must have length equal to (or g.t.) `num_threads`.

```
ptask_context_t *ptask_init(
	void *(*worker)(void *arg, void *item),
	void *worker_arg[],
	int64_t num_threads,
	int64_t queue_size);
```

### ptask_clean

Cleanup the context.

```
void ptask_clean(
	ptask_context_t *ctx);
```

### ptask_parallel

Execute worker function (first argument of `ptask_init`) with `worker_arg[thread_id]` in the first argument and `items[thread_id]` in the second argument (if `items` is not `NULL`). The return value will be stored to `results[thread_id]` if `results` is not `NULL`.

```
int ptask_parallel(
	ptask_context_t *ctx,
	void *items[],
	void *results[]);
```

### ptask_stream

Scatter items from `source` to the parallel `worker`, gather the results to `drain`. The `source` and `drain` will be called `source_arg` and `drain_arg` in the first argument respectively.

```
int ptask_stream(
	ptask_context_t *ctx,
	void *(*source)(void *arg),
	void *source_arg,
	void (*drain)(void *arg, void *result),
	void *drain_arg,
	int64_t bulk_elems);
```

