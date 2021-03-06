/*

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef TENSORFLOW_SERVING_SERVABLES_XGBOOST_PREDICT_IMPL_H_
#define TENSORFLOW_SERVING_SERVABLES_XGBOOST_PREDICT_IMPL_H_

#include "tensorflow/core/lib/core/status.h"
#include "tensorflow_serving/apis/predict.pb.h"
#include "tensorflow_serving/model_servers/server_core.h"

#include <bvar/bvar.h>

namespace tensorflow {
namespace serving {

class XgboostPredictor {
public:
  XgboostPredictor();

  Status Predict(ServerCore *core, const PredictRequest &request,
                 PredictResponse *response);

  Status PredictWithModelSpec(ServerCore *core, const ModelSpec &model_spec,
                              const PredictRequest &request,
                              PredictResponse *response);

  ~XgboostPredictor();

private:
  static bvar::LatencyRecorder xgboost_latency_recorder;
};
} // namespace serving
} // namespace tensorflow

#endif // TENSORFLOW_SERVING_SERVABLES_XGBOOST_PREDICT_IMPL_H_
