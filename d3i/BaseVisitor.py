import d3i
from Engine import Session

class BaseVisitor:

    def visitd3(self, d3: d3i.domain, session: Session):
        pass

    def visitDomain(self, domain: d3i.domain, session: Session):
        pass

    def visitDirective(self, directive: d3i.directive, session: Session):
        pass

    def visitContext(self, context: d3i.context, session: Session):
        pass

    def visitEvent(self, event: d3i.event, session: Session):
        pass

    def visitEventMember(self, eventMember: d3i.event_member, session: Session, parentEvent: d3i.event):
        pass

    def visitEnum(self, domain: d3i.enum, session: Session):
        pass

    def visitEnumElement(self, enum_element: d3i.enum_element, session: Session, parentEnum: d3i.enum):
        pass

    def visitValueObject(self, value_object: d3i.value_object, session: Session):
        pass

    def visitValueObjectMember(self, domain: d3i.value_object_member, session: Session, parentValueObject: d3i.value_object):
        pass

    def visitEnity(self, entity: d3i.entity, session: Session):
        pass

    def visitEnityMember(self, entity: d3i.entity_member, session: Session, parentEntity: d3i.entity):
        pass

    def visitAggregate(self, aggregate: d3i.aggregate, session: Session):
        pass

    def visitAggregateEntity(self, aggregate: d3i.aggregate_entity, session: Session, parentAggregate: d3i.aggregate):
        pass

    def visitRepository(self, repository: d3i.repository, session: Session):
        pass

    def visitAcl(self, acl: d3i.acl, session: Session):
        pass

    def visitService(self, service: d3i.service, session: Session):
        pass

    def visitInterface(self, interface: d3i.interface, session: Session):
        pass

    def visitOperation(self, operation: d3i.operation, session: Session):
        pass

    def visitOperationParam(self, operation_param: d3i.operation_param, session: Session,parentOpeartion: d3i.operation):
        pass

    def visitOperationReturn(self, operation_return: d3i.operation_return, session: Session,parentOpeartion: d3i.operation):
        pass

    def visitMethod(self, method: d3i.method, session: Session):
        pass

    def visitMethodParam(self, method_param: d3i.method_param, session: Session, parentMethod: d3i.method):
        pass

    def visitPrimitiveType(self, primtiveType: d3i.primitive_type, session: Session ):
        pass

    def visitReferenceType(self, reference_type: d3i.reference_type, session: Session ):
        pass

    def visitListType(self, list_type: d3i.list_type, session: Session ):
        pass

    def visitMapType(self, map_type: d3i.map_type, session: Session ):
        pass
