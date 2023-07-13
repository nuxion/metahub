# Metahub

MetaHub pretends to be a Meta Store server to track different assets related to different projects. It doesn store the real data, only where is this data and what it could have.  

It is built for different uses case in mind, but mostly to work with data and ML problems. 

The main use case and how it was started is to have a metadata store for objects stored cross different buckets and different Cloud providers.

In regards to that, the project has three main entities:

- Object: is a single object, what is finally stored in a Object Storage (s3, google objects, ...)
- Bucket: A real bucket, but in some way could be anything containing the objects, 
- Collection: this entity only exist on the domain of **metahub**. Their purpose is to bring together objects belonging to a "dataset" but for some reason their are in different places. 

Those entities are not stricted to the cloud.

In a local implementation, objects could be files, buckets folders and a collection a way to say: "USD Currency History" which groups Excel files distributed in different "buckets"/"folders". 

Finally this is still a work in progress. 

Keep in touch for any doubt or suggestion. Any comment is welcome.  


## How it is structured

I tried to put each domain in a seperate app:

- core: mainly project related data
- assets: Objects, Bucket and Collections
- models: not implemented yet. Related to location and metadata for ML Models. 
- tasks: not implemented yet. Related to executions results, history a so oon. 
- cloud-resources: not implemented yet. Related to virtual machines, services, etc.
- code: not implemented yet. it could be related to notebook files, github repositories... etc

## References

- Based on [Django Template](https://github.com/nuxion/django-template)

## License

`metahub` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
